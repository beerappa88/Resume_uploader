from fastapi import FastAPI, Form, UploadFile, HTTPException, File
from pydantic import BaseModel
import os
import re
from fastapi.responses import JSONResponse
from database import Base, engine, UPLOAD_FOLDER, SessionLocal
from models import Resume


app = FastAPI()

# Secure filename
def secure_filename(filename: str) -> str:
    filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)  # Replace invalid characters with '_'	
    return filename.strip().strip(".")  # Remove leading/trailing periods


# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic model for validation
class ResumeSubmission(BaseModel):
    name: str
    phone: str
    email: str
    institute: str


@app.post("/submit")
async def submit_resume(
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    institute: str = Form(...),
    resume: UploadFile = File(...)
):
    # Validate file
    if not resume.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        # Secure and save the file to disk
        filename = secure_filename(resume.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)


        with open(filepath, "wb") as f:
            content = await resume.read()
            f.write(content)

        # Get file size in KB
        filesize = len(content) // 1024

        # Save metadata to database
        db = SessionLocal()
        resume_entry = Resume(
            name=name,
            phone=phone,
            email=email,
            institute=institute,
            filename=filename,
            filepath=filepath,
            filesize=filesize
        )
        db.add(resume_entry)
        db.commit()
        db.close()

        return JSONResponse(content={"message": "Resume submitted successfully!"}, status_code=201)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@app.get("/resumes")
def get_resumes():
    try:
        db = SessionLocal()
        resumes = db.query(Resume).all()
        db.close()

        result = [
            {
                "id": r.id,
                "name": r.name,
                "phone": r.phone,
                "email": r.email,
                "institute": r.institute,
                "filename": r.filename,
                "filepath": r.filepath,
                "filesize": r.filesize
            } for r in resumes
        ]

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
