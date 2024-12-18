# Resume Submission API

This project is a FastAPI-based web application that allows users to submit their resumes. The resumes are stored on the server's disk, and their metadata is saved in a PostgreSQL database.

---

## Features
- Submit resumes via a form.
- Store uploaded resumes as PDF files on disk.
- Save metadata (name, email, phone, institute, file size, file path) in the PostgreSQL database.
- Retrieve all submitted resumes via an API endpoint.

---

## File Structure
```
├── main.py         # Entry point of the application
├── database.py     # Database configuration and setup
├── models.py       # SQLAlchemy models
```

---

## Requirements

### Prerequisites
- Python 3.12+
- PostgreSQL database

### Python Dependencies
Install required Python libraries:
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/resume-api.git
cd resume-api
```

### 2. Configure the Database
- Update `DATABASE_URL` in `database.py` with your PostgreSQL credentials:
  ```python
  DATABASE_URL = "postgresql://<username>:<password>@<host>/<database_name>"
  ```
- Create the database tables:
  ```bash
  python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
  ```

### 3. Run the Application
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

### 4. Access the Application
- Visit the FastAPI documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Submit resumes and test endpoints.

---

## API Endpoints

### POST `/submit`
Submit a resume with metadata.

#### Request (Multipart Form-Data):
| Field      | Type   | Description          |
|------------|--------|----------------------|
| `name`     | String | Full name            |
| `phone`    | String | Phone number         |
| `email`    | String | Email address        |
| `institute`| String | Institute name (optional) |
| `resume`   | File   | PDF file of the resume |

#### Response:
```json
{
  "message": "Resume submitted successfully!"
}
```

### GET `/resumes`
Retrieve all submitted resumes.

#### Response:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "phone": "1234567890",
    "email": "john@example.com",
    "institute": "Example University",
    "filename": "resume.pdf",
    "filepath": "./uploads\resume.pdf",
    "filesize": 12345
  }
]
```



