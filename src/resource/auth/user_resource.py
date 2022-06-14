from src.resource.base import BaseResource
from src.services.user_service import UserService
from src.shared.exception.ledger_exception import LedgerException
from src.shared.response.response_data import response_payload


class UserResource(BaseResource):

    def get(self):
        try:
            user_service = UserService()
            response = user_service.get_users(self.message_bus.uow)
            return response, 200
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            print(ex)
            return response_payload(None, ex.args, ex.args[1], False), 400


class UserDetailResource(BaseResource):

    def get(self, emp_id):
        user_service = UserService()
        user = user_service.get_user_by_emp_id(emp_id, self.message_bus.uow)
        return user

    def put(self, emp_id):
        user_service = UserService()
        user = user_service.update_user_by_emp_id(emp_id, self.message_bus.uow)
        return user

    def delete(self, emp_id):
        user_service = UserService()
        user = user_service.delete_user_by_emp_id(emp_id, self.message_bus.uow)
        return user
