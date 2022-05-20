from flask_restful import Resource
from flask import request
from src.database.temp_db import users
from src.services import user


class UserResource(Resource):

    def get(self):
        response = user.get_all_user()
        return response


class UserDetailResource(Resource):

    def get(self, user_id):
        data = request.get_json()
        response = user.get_user(user_id)
        return response

    def put(self, user_id):
        data = request.get_json()
        response = user.update_user(user_id)
        return response

    def delete(self, user_id):
        data = request.get_json()
        response = user.delete_user(user_id)
        return response
