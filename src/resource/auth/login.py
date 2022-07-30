from flask import request

from src.resource.base import BaseResource
from src.services.auth.loginservice import LoginService
from src.shared.exception.ledger_exception import LedgerException
from src.shared.response.response_data import response_payload

login_service: LoginService = LoginService()


class LoginResource(BaseResource):

    def post(self):
        try:
            data = request.get_json()
            token = login_service.validate_user(
                data,
                self.message_bus.uow,
                self.message_bus.redis
            )
            return response_payload({'token': token}), 200

        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args[0], ex.args[1], False), 500

