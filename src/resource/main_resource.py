from flask import request
from flask_restful import Resource

from src.bootstrap import main_bootstrap
from src.database.interface.sql_uow import SqlUow
from src.services.loginservice import LoginService
from src.services.user_service import UserService

uow: SqlUow = main_bootstrap.bootstrap()  #creating circular dependency


class RegisterResource(Resource):

    def post(self):
        data = request.get_json()
        user_service = UserService()
        response = user_service.create_user(data, uow)
        return response


class LoginResource(Resource):

    def post(self):
        data = request.get_json()
        return data


class UserResource(Resource):

    def get(self):
        user_service = UserService()
        response = user_service.get_users(uow)
        return response


class UserDetailResource(Resource):

    def get(self, emp_id):
        user_service = UserService()
        user = user_service.get_user_by_emp_id(emp_id, uow)
        return user

    def put(self, emp_id):
        user_service = UserService()
        user = user_service.update_user_by_emp_id(emp_id, uow)
        return user

    def delete(self, emp_id):
        user_service = UserService()
        user = user_service.delete_user_by_emp_id(emp_id, uow)
        return user


