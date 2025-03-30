from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.infrastructure.database.config import Base

class UserModel(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)

