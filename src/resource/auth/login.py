from flask import request

from src.resource.base import BaseResource


class LoginResource(BaseResource):

    def post(self):
        data = request.get_json()
        return data
