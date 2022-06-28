from src.repository.postgresql.admin.user import UserPostRepository


class LoginService:

    def __init__(self):
        self.userRepository = UserPostRepository()



