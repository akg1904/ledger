from flask import request

from src.resource.base import BaseResource
from src.services.user_service import UserService


class RegisterResource(BaseResource):

    def post(self):
        data = request.get_json()
        user_service = UserService()
        response = user_service.create_user(data, self.message_bus.uow)
        return response
