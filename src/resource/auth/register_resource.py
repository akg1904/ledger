from flask import request

from src.resource.base import BaseResource
from src.services.auth.user_service import UserService
from src.shared.exception.ledger_exception import LedgerException
from src.shared.response.response_data import response_payload


class RegisterResource(BaseResource):

    def post(self):
        try:
            data = request.get_json()
            user_service = UserService()
            response = user_service.create_user(data, self.message_bus.uow)
            return response_payload(response)

        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args[0], ex.args[1], False), 500
