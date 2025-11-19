from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DB_URL  # Absolute import from config

# SQLAlchemy setup
engine = create_engine(DB_URL, connect_args={"check_same_thread": False} if "sqlite" in DB_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency function for FastAPI or other usage
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
