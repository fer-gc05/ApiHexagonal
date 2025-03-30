from src.domain.entities.user import User
from src.application.ports.user_repository import UserRepository
from src.domain.exceptions import InvalidCredentialsException

class LoginUser:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> User:
        try:
            user = self.user_repository.get_user_by_email(email)
            if not user or not user.check_password(password):
                raise InvalidCredentialsException('Email o contraseña incorrectos')
            return user
        except InvalidCredentialsException as e:
            raise e
