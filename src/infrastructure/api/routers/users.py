from fastapi import APIRouter, Depends
from src.infrastructure.api.auth import get_current_user
from src.infrastructure.api.schemas.user import UserUpdate, UserResponse
from src.domain.entities.user import User
from src.infrastructure.api.dependencies import get_update_user_use_case
from src.application.use_cases.user.update_user import UpdateUser

router = APIRouter()

@router.put('/me')
def update_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    use_case: UpdateUser = Depends(get_update_user_use_case)
):
    updated_user = use_case.execute(current_user.id, user_update.username, user_update.email)
    return {'Usuario actualizado': updated_user}