from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import yaml

# Load config.yml
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# Database configuration
engine = create_engine(config["DATABASE_URL"])
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ensure upload directory exists
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

