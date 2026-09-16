from sqlalchemy.orm import Session

from models.user_model import User
from repository.user_repository import UserRepository
from auth import verify_password, get_password_hash


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def register_user(self, db: Session, user):

        existing_user = self.repository.get_user_by_username(
            db,
            user.username
        )

        if existing_user:
            return None

        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password_hash(user.password)
        )

        created_user = self.repository.create_user(db, new_user)

        return created_user

    def authenticate_user(self, db: Session, username: str, password: str):

        user = self.repository.get_user_by_username(db, username)

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return user