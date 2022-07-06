from flask import request

from src.resource.base import BaseResource
from src.services.admin.rate import RateService
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.ledger_exception import LedgerException
from src.shared.response.response_data import response_payload

rate_service = RateService()


class RateResource(BaseResource):

    def get(self, **kwargs):
        try:
            response = rate_service.get_rate_by_item_code(kwargs['item_code'], self.message_bus.uow)
            return response_payload(response), 200
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 4000, False), 400

    def post(self, **kwargs):
        try:
            data = request.get_json()
            response = rate_service.create_rate(data, kwargs['item_code'], self.message_bus.uow)
            return response_payload(response), 200
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 4000, False), 400


class RateDetailResource(BaseResource):

    def get(self, **kwargs):
        try:
            response = rate_service.get_rate_by_id(kwargs['rate_id'], kwargs['item_code'], self.message_bus.uow)
            return response
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 4000, False), 400

    def put(self, **kwargs):
        try:
            data = request.get_json()
            response = rate_service.update_rate_by_id(kwargs['rate_id'], kwargs['item_code'], data, self.message_bus.uow)
            return response_payload(response, "Record Updated")
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 4000, False), 400

    def delete(self, **kwargs):
        try:
            response = rate_service.delete_rate_by_id(kwargs['rate_id'], self.message_bus.uow)
            return response_payload(None, "Record Deleted")
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 4000, False), 400



