from src.repository.interface.user import UserInterface
from src.database import temp_db


class UserRaw(UserInterface):

    def create_user(self, data):
        data['id'] = len(temp_db.users) + 1
        temp_db.users.append(data)
        print(temp_db.users)
        return data

    def get_all_user(self):
        return {'user': temp_db.users}

    def delete_user_by_id(self, ids):
        users = temp_db.users
        required_index = -1

        for index, user in enumerate(users):
            if user['id'] == ids:
                required_index = index
                del users[index]
                break

        return users

    def update_user_by_id(self, ids):
        users = temp_db.users
        required_user = None

        for index, user in enumerate(users):
            if user['id'] == ids:
                required_user = user
                required_user["name"] = "abhishek"

        return required_user

    def get_user_by_id(self, ids):
        users = temp_db.users
        required_user = None

        for user in users:
            if user['id'] == ids:
                required_user = user

        return required_user



