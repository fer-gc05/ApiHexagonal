from fastapi import APIRouter, Depends, HTTPException
from src.infrastructure.api.auth import get_current_user
from src.infrastructure.api.schemas.post import PostCreate, PostUpdate, PostResponse
from src.domain.entities.user import User
from src.infrastructure.api.dependencies import get_create_post_use_case, get_update_post_use_case, get_delete_post_use_case, get_post_repo
from src.application.use_cases.post.create_post import CreatePost
from src.application.use_cases.post.update_post import UpdatePost
from src.application.use_cases.post.delete_post import DeletePost
from src.infrastructure.repositories.post_repository_sqlalchemy import PostRepositorySQLAlchemy

router = APIRouter()

@router.post("/")
def create_post(
    post: PostCreate,
    current_user: User = Depends(get_current_user),
    use_case: CreatePost = Depends(get_create_post_use_case)
):
    created_post = use_case.execute(post.title, post.content, current_user.id)
    return {'Post creado con éxito': created_post}

@router.get("/")
def list_posts(
    post_repo: PostRepositorySQLAlchemy = Depends(get_post_repo)
):
    return {'Posts': post_repo.get_all_posts()}

@router.put("/{post_id}")
def update_post(
    post_id: int,
    post_update: PostUpdate,
    current_user: User = Depends(get_current_user),
    use_case: UpdatePost = Depends(get_update_post_use_case)
):
    updated_post = use_case.execute(post_id, post_update.title, post_update.content)
    if updated_post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")
    return {'Post actualizado con éxito': updated_post}


@router.delete('/{post_id}')
def delete_post(
        post_id: int,
        current_user: User = Depends(get_current_user),
        use_case: DeletePost = Depends(get_delete_post_use_case),
        post_repo: PostRepositorySQLAlchemy = Depends(get_post_repo)
):
    try:
        post = post_repo.get_post_by_id(post_id)
    except ValueError:
        raise HTTPException(status_code=404, detail='Post no encontrado')

    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail='Usuario no autorizado para eliminar este post')

    success = use_case.execute(post_id)
    if not success:
        raise HTTPException(status_code=500, detail='Error al eliminar el post')

    return {'message": "Post eliminado con éxito'}