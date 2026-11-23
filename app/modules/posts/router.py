from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.modules.posts import service, schemas

router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/", response_model=list[schemas.PostOut])
def list_posts(db: Session = Depends(get_db)):
    return service.list_all(db)

@router.post("/", response_model=schemas.PostOut, status_code=201)
def create_post(data: schemas.PostCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return service.create(db, data, user)

@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    service.delete(db, post_id, user)