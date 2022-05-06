from flask_restful import Resource
from flask import request

from src.database.db.db_instance import DBInstance
from src.services.loginservice import validate_user

conn = DBInstance().db
user = ' '


class LoginResource(Resource):

    def get(self):
        # data = request.get_json()
        return {'message': 'Login working'}

    def post(self):
        data = request.get_json()
        print(data)
        response = validate_user(data)

        return response
