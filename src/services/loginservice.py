
from src.repository.sqlite.user import UserSqlite


class LoginService:

    def __init__(self):
        self.userRepository = UserSqlite()

    def create_user(self, data: dict, uow):
        response = None
        with uow:
            response = self.userRepository.create_user(data, uow)
            uow.commit()

        return response

