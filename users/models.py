from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime

from settings.settings import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    last_name = Column(String(20), nullable=False)
    first_name = Column(String(200), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
