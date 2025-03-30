from src.domain.entities.user import User
from src.application.ports.user_repository import UserRepository

class RegisterUser:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, username: str, email: str, password: str) -> User:
        try:
            existing_user = self.user_repository.get_user_by_email(email)
            if existing_user:
                raise Exception('El usuario ya existe')
            created_user = self.user_repository.create_user(username=username, email=email, password=password)
            if not created_user:
                raise Exception('No se pudo crear el usuario')
            return created_user
        except Exception as e:
            raise e