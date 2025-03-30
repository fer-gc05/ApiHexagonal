from pydantic import BaseModel, Field

class Comment(BaseModel):
    id: int | None = None
    content: str = Field(..., min_length=1, max_length=500)
    user_id: int
    post_id: int

    class Config:
        from_attributes = True