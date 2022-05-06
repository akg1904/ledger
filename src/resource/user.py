from flask_restful import Resource
from src.database.temp_db import users

class UserResource(Resource):

    def get(self):

        return {'user': users}
