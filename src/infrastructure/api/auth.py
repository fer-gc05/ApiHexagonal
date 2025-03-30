from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.config.config import config
from src.domain.entities.user import User
from src.infrastructure.repositories.user_repository_sqlalchemy import UserRepositorySQLAlchemy
from src.infrastructure.database.config import get_db
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Credenciales de autenticación inválidas',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=['HS256'])
        user_id: int = payload.get('sub')
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user_repo = UserRepositorySQLAlchemy(db)
    user = user_repo.get_user_by_id(user_id)
    if user is None:
        raise credentials_exception
    return user