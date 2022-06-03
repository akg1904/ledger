from flask_restful import Resource
from flask import request

#creating circular dependency
from src.bootstrap import main_bootstrap
from src.database.interface.sql_uow import SqlUow
from src.services.loginservice import LoginService


uow: SqlUow = main_bootstrap.bootstrap()  #creating circular dependency


class LoginResource(Resource):

    def get(self):
        return {'message': 'Login working'}

    def post(self):
        data = request.get_json()
        login_service = LoginService()
        response = login_service.create_user(data, uow)
        return response
