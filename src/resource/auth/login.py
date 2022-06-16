from flask import request

from src.resource.base import BaseResource
from src.shared.exception.ledger_exception import LedgerException
from src.shared.response.response_data import response_payload


class LoginResource(BaseResource):

    def post(self):
        try:
            data = request.get_json()
            return response_payload(data), 200
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args[0], ex.args[1], False), 500

