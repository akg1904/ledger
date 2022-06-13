from src.resource.base import BaseResource
from src.services.user_service import UserService


class UserResource(BaseResource):

    def get(self):
        user_service = UserService()
        response = user_service.get_users(self.message_bus.uow)
        return response


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
