from fastapi import APIRouter, Depends, HTTPException
from src.infrastructure.api.auth import get_current_user
from src.infrastructure.api.schemas.comment import CommentCreate, CommentResponse
from src.domain.entities.user import User
from src.infrastructure.api.dependencies import get_create_comment_use_case, get_delete_comment_use_case, get_comment_repo
from src.application.use_cases.comment.create_comment import CreateComment
from src.application.use_cases.comment.delete_comment import DeleteComment
from src.infrastructure.repositories.comment_repository_sqlalchemy import CommentRepositorySQLAlchemy

router = APIRouter()

@router.post('/')
def create_comment(
    post_id: int,
    comment: CommentCreate,
    current_user: User = Depends(get_current_user),
    use_case: CreateComment = Depends(get_create_comment_use_case)
):
    created_comment = use_case.execute(comment.content, current_user.id, post_id)
    return {'Comentario creado con éxito': created_comment}

@router.get('/')
def list_comments(
    post_id: int,
    comment_repo: CommentRepositorySQLAlchemy = Depends(get_comment_repo)
):
    return {'Comentarios': comment_repo.get_comments_by_post_id(post_id)}

@router.delete('/{comment_id}')
def delete_comment(
    comment_id: int,
    current_user: User = Depends(get_current_user),
    use_case: DeleteComment = Depends(get_delete_comment_use_case),
    comment_repo: CommentRepositorySQLAlchemy = Depends(get_comment_repo)
):
    comment = comment_repo.get_comment_by_id(comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")
    success = use_case.execute(comment_id)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to delete comment")
    return {'message': 'Comentario eliminado con éxito'}