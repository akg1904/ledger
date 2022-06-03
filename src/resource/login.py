from flask_restful import Resource
from flask import request

#creating circular dependency
# from src.bootstrap import main_bootstrap
from src.database.interface.sql_uow import SqlUow
from src.services.loginservice import LoginService


login_service = LoginService()
# uow: SqlUow = main_bootstrap.bootstrap()  #creating circular dependency
uow = None

class LoginResource(Resource):

    def get(self):
        login_service.create_user(uow)
        return {'message': 'Login working'}

    def post(self):
        data = request.get_json()
        print(data)
        response = data

        return response
