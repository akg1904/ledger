from flask import request
from flask_restful import Resource

from src.resource.base import BaseResource
from src.services.loginservice import LoginService
from src.services.user_service import UserService


class RegisterResource(BaseResource):

    def post(self):
        data = request.get_json()
        user_service = UserService()
        response = user_service.create_user(data, self.message_bus.uow)
        return response


class LoginResource(BaseResource):

    def post(self):
        data = request.get_json()
        return data


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


