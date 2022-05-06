from src.database import temp_db
from src.repository.interface.user import UserInterface
from src.repository.raw_file.user import UserRaw
from src.repository.sqlite.user import UserSqlite

user_repository: UserInterface = UserRaw()


def register_user(data):
    response = user_repository.create_user(data)
    return response


