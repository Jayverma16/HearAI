from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    transcript = Column(Text)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
