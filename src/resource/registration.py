from flask_restful import Resource
from src.database.temp_db import users
from flask import request
from src.services import registerservice


class Registration(Resource):

    def get(self):
        pass

    def post(self):
        data = request.get_json()
        response = registerservice.register_user(data)
        return response

    