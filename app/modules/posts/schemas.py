from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    body: str = ""

class PostOut(BaseModel):
    id: int
    title: str
    body: str
    author_id: int
    class Config: from_attributes = True