from flask_restful import Resource


class LogoutResource(Resource):

    def get(self):
        return {"message": "You are being Logout"}

