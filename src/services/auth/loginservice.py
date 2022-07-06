from src.repository.postgresql.auth.user import UserPostRepository


class LoginService:

    def __init__(self):
        self.userRepository = UserPostRepository()



