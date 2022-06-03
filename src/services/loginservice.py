
from src.repository.sqlite.user import UserSqlite


class LoginService:

    def __init__(self):
        self.userRepository = UserSqlite()

    def create_user(self, uow):
        with uow:
            self.userRepository.create_user('hello', uow)
            uow.commit()

