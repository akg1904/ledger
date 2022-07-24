
from flask import request

from src.resource.base import BaseResource
from src.services.Interface.admin.Stock import StockServiceInterface
from src.services.admin.stock import StockService
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.ledger_exception import LedgerException
from src.shared.response.response_data import response_payload

stock_service: StockServiceInterface = StockService()


class StockResource(BaseResource):

    def get(self, **kwargs):
        try:
            response = stock_service.get_stock_by_item_code(kwargs['item_code'], self.message_bus.uow)
            return response_payload(response, "Stock Record"), 200
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 4000, False), 400

    def post(self, **kwargs):
        try:
            data = request.get_json()
            print(data)
            response = stock_service.create_stock(data, kwargs['item_code'], kwargs['rate_id'], self.message_bus.uow)
            return response_payload(response, "Record Created"), 200
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 4000, False), 400


class StockDetailResource(BaseResource):

    def get(self, **kwargs):
        response = stock_service.get_stock_by_id(kwargs['id'], kwargs['item_code'], self.message_bus.uow)
        return response

    def put(self, **kwargs):
        data = request.get_json()
        response = stock_service.update_stock_by_id(kwargs['id'], kwargs['item_code'], data, self.message_bus.uow)
        return response

    def delete(self, **kwargs):
        response = stock_service.delete_stock_by_id(kwargs['id'], kwargs['item_code'], self.message_bus.uow)
        return response

