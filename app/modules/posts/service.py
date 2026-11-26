from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.post import Post
from app.models.user import User
from app.modules.posts.schemas import PostCreate
from app.tasks.notifications import send_notification

def create(db: Session, data: PostCreate, user: User) -> Post:
    post = Post(**data.model_dump(), author_id=user.id)
    db.add(post)
    db.commit()
    db.refresh(post)
    
    send_notification.delay(user.email, post.id)
    return post

def list_all(db: Session): 
    return db.query(Post).all()

def delete(db: Session, post_id: int, user: User):
    post = db.get(Post, post_id)
    if not post: 
        raise HTTPException(404, "Not found")

    if post.author_id != user.id and user.role != "admin":
        raise HTTPException(403, "Forbidden")
    db.delete(post)
    db.commit()