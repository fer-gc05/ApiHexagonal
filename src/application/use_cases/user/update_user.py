from src.domain.entities.user import User
from src.application.ports.user_repository import UserRepository
from src.domain.exceptions import UserNotFoundException
from pydantic import EmailStr

class UpdateUser:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, id: int, username: str | None, email: EmailStr | None) -> User:
        existing_user = self.user_repository.get_user_by_id(id)
        if not existing_user:
            raise UserNotFoundException('El usuario no existe')
        updated_data = existing_user.model_dump()

        if username is not None:
            updated_data["username"] = username
        if email is not None:
            updated_data["email"] = email
        updated_user = User(**updated_data)

        updated_user = self.user_repository.update_user(updated_user)
        if not updated_user:
            raise Exception('No se pudo actualizar el usuario')

        return updated_user