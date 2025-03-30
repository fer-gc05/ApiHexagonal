from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from datetime import datetime, timedelta
from src.config.config import config
from src.infrastructure.api.schemas.user import UserCreate, UserLogin, UserResponse, Token
from src.infrastructure.api.dependencies import get_register_user_use_case, get_login_user_use_case
from src.application.use_cases.user.register_user import RegisterUser
from src.application.use_cases.user.login_user import LoginUser

router = APIRouter()

@router.post('/register', response_model=UserResponse)
def register_user(
    user: UserCreate,
    use_case: RegisterUser = Depends(get_register_user_use_case)
):
    try:
        created_user = use_case.execute(user.username, user.email, user.password)
        return created_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post('/login', response_model=Token)
def login_user(
    login: UserLogin,
    use_case: LoginUser = Depends(get_login_user_use_case)
):
    user = use_case.execute(login.email, login.password)
    access_token_expires = timedelta(minutes=30)
    access_token = jwt.encode(
        {'sub': str(user.id), 'exp': datetime.utcnow() + access_token_expires},
        config.SECRET_KEY,
        algorithm='HS256'
    )
    return {'access_token': access_token, 'token_type': 'bearer'}