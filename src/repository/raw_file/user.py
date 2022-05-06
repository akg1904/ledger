from src.repository.interface.user import UserInterface
from src.database import temp_db


class UserRaw(UserInterface):

    def create_user(self, data):
        data['id'] = len(temp_db.users) + 1
        temp_db.users.append(data)
        return data

    def delete_user_by_id(self, id):
        pass

    def update_user_by_id(self, id):
        pass

    def get_user_by_id(self, id):
        pass

    def get_all_user(self):
        pass