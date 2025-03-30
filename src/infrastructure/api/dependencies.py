from sqlalchemy.orm import Session
from src.infrastructure.database.config import get_db
from src.infrastructure.repositories.user_repository_sqlalchemy import UserRepositorySQLAlchemy
from src.infrastructure.repositories.post_repository_sqlalchemy import PostRepositorySQLAlchemy
from src.infrastructure.repositories.comment_repository_sqlalchemy import CommentRepositorySQLAlchemy
from src.application.use_cases.user.register_user import RegisterUser
from src.application.use_cases.user.login_user import LoginUser
from src.application.use_cases.user.update_user import UpdateUser
from src.application.use_cases.post.create_post import CreatePost
from src.application.use_cases.post.update_post import UpdatePost
from src.application.use_cases.post.delete_post import DeletePost
from src.application.use_cases.comment.create_comment import CreateComment
from src.application.use_cases.comment.delete_comment import DeleteComment
from fastapi import Depends

def get_register_user_use_case(db: Session = Depends(get_db)) -> RegisterUser:
    return RegisterUser(UserRepositorySQLAlchemy(db))

def get_login_user_use_case(db: Session = Depends(get_db)) -> LoginUser:
    return LoginUser(UserRepositorySQLAlchemy(db))

def get_update_user_use_case(db: Session = Depends(get_db)) -> UpdateUser:
    return UpdateUser(UserRepositorySQLAlchemy(db))

def get_create_post_use_case(db: Session = Depends(get_db)) -> CreatePost:
    return CreatePost(PostRepositorySQLAlchemy(db))

def get_update_post_use_case(db: Session = Depends(get_db)) -> UpdatePost:
    return UpdatePost(PostRepositorySQLAlchemy(db))

def get_delete_post_use_case(db: Session = Depends(get_db)) -> DeletePost:
    return DeletePost(PostRepositorySQLAlchemy(db))

def get_create_comment_use_case(db: Session = Depends(get_db)) -> CreateComment:
    post_repo = PostRepositorySQLAlchemy(db)
    comment_repo = CommentRepositorySQLAlchemy(db)
    return CreateComment(comment_repo, post_repo)

def get_delete_comment_use_case(db: Session = Depends(get_db)) -> DeleteComment:
    return DeleteComment(CommentRepositorySQLAlchemy(db))

def get_post_repo(db: Session = Depends(get_db)) -> PostRepositorySQLAlchemy:
    return PostRepositorySQLAlchemy(db)

def get_comment_repo(db: Session = Depends(get_db)) -> CommentRepositorySQLAlchemy:
    return CommentRepositorySQLAlchemy(db)