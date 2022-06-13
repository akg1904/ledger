from src.database.interface.sql_uow import SqlUow
from src.repository.postgresql.user import UserPostRepository


class UserService:

    def __init__(self):
        self.userRepository = UserPostRepository()

    def create_user(self, data: dict, uow: SqlUow):
        user = None
        with uow:
            user = self.userRepository.get_user_by_username(data['user_name'], uow)
            if not user:
                emp_id = self.userRepository.create_user(data, uow)
                uow.commit()
                created_user = self.userRepository.get_user_by_emp_id(emp_id, uow)
                if not created_user:
                    return {'message': 'Failed to create user'}
                return created_user

            else:
                return {'message': 'User already exists'}
        return user

    def get_user_by_username(self, username, uow: SqlUow):
        user = None
        with uow:
            user = self.userRepository.get_user_by_username(username, uow)
        return user

    def get_user_by_emp_id(self, emp_id, uow: SqlUow):
        user = None
        with uow:
            user = self.userRepository.get_user_by_emp_id(emp_id, uow)
        return user

    def get_users(self, uow: SqlUow):
        users = []
        with uow:
            users = self.userRepository.get_all_user(uow)

        return users

    def update_user_by_emp_id(self, emp_id, uow: SqlUow):
        user = None
        with uow:
            user = self.userRepository.update_user_by_emp_id(emp_id, uow)
            uow.commit()
        return user

    def delete_user_by_emp_id(self, emp_id, uow:SqlUow):
        user = None
        with uow:
            user = self.userRepository.delete_user_by_id(emp_id, uow)
            uow.commit()
        return user

