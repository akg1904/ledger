from src.repository.interface.user import UserInterface


class UserSqlite(UserInterface):

    def create_user(self, data):
        query = "Insert into user (username, password) values (%s, %s)".format(data['username'], data['password'])
        pass

    def delete_user_by_id(self, id):
        pass

    def update_user_by_id(self, id):
        pass

    def get_user_by_id(self, id):
        pass

    def get_all_user(self):
        pass