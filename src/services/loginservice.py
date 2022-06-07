from src.repository.postgresql.user import UserPostRepository


class LoginService:

    def __init__(self):
        self.userRepository = UserPostRepository()



