from sqlalchemy import Column, Integer, String
from database import Base

# Database Model
class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
    institute = Column(String(150), nullable=True)
    filename = Column(String(200), nullable=False)
    filepath = Column(String(300), nullable=False)
    filesize = Column(Integer, nullable=False)