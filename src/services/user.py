from src.repository.interface.user import UserInterface
from src.repository.raw_file.user import UserRaw
from src.database.temp_db import users


user_repository: UserInterface = UserRaw()


def get_all_user():
    response = user_repository.get_all_user()
    return response


def update_user(ids):
    response = user_repository.update_user_by_id(ids)
    return response


def get_user(ids):
    response = user_repository.get_user_by_id(ids)
    return response


def delete_user(ids):
    response = user_repository.delete_user_by_id(ids)
    return response
