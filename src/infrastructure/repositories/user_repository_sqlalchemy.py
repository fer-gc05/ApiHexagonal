from src.domain.entities.user import User
from src.application.ports.user_repository import UserRepository
from src.infrastructure.database.models.user import UserModel
from sqlalchemy.orm import Session

class UserRepositorySQLAlchemy(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str, password: str) -> User:

        user = User.create(username=username, email=email, password=password)
        db_user = UserModel(username=user.username, email=user.email, password_hash=user.password_hash)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User.model_validate(db_user)

    def get_user_by_id(self, user_id: int) -> User | None:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        return User.model_validate(db_user) if db_user else None

    def get_user_by_email(self, email: str) -> User | None:
        db_user = self.db.query(UserModel).filter(UserModel.email == email).first()
        return User.model_validate(db_user) if db_user else None

    def update_user(self, user: User) -> User:
        db_user = self.db.query(UserModel).filter(UserModel.id == user.id).first()
        if db_user:
            for key, value in user.model_dump(exclude={"id"}).items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
            return User.model_validate(db_user)
        return user

    def get_all_users(self) -> list[User]:
        db_users = self.db.query(UserModel).all()
        return [User.model_validate(db_user) for db_user in db_users]

    def delete_user(self, user_id: int) -> bool:
        db_user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False