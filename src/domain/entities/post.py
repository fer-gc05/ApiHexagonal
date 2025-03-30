from pydantic import BaseModel, Field

class Post(BaseModel):

    id: int | None = None
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=10, max_length=5000)
    user_id: int

    class Config:
        from_attributes = True