from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.postgresql.auth.user import UserPostRepository
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class UserService:

    def __init__(self):
        self.userRepository = UserPostRepository()

    def create_user(self, data: dict, uow: SqlUow):
        user = None
        with uow:
            user = self.userRepository.get_user_by_username(data['user_name'], uow)
            if user:
                raise LedgerException(ErrorCode.USER_EXISTS, ErrorMessage.USER_EXISTS)

            emp_id = self.userRepository.create_user(data, uow)
            uow.commit()
            created_user = self.userRepository.get_user_by_emp_id(emp_id, uow)
            if not created_user:
                raise LedgerException(ErrorCode.USER_CREATION_FAILED, ErrorMessage.USER_CREATION_FAILED)

            return created_user

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
            # raise LedgerException(ErrorCode.FAILURE, ErrorMessage.FAILURE)
            # raise Exception("Exception raised", 5001)
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

