from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.infrastructure.database.config import Base

class PostModel(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(String(5000), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
