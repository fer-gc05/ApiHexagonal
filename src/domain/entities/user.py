from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from bcrypt import hashpw, checkpw, gensalt

class User(BaseModel):

    id: int | None = None
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password_hash: str

    @classmethod
    def create(cls, username: str, email: str, password: str):
        hashed_password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
        return cls(username=username, email=email, password_hash=hashed_password)

    def check_password(self, password: str) -> bool:
        return checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    class Config:
        from_attributes = True
