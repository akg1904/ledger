from flask import request

from src.database.interface.sql_uow import SqlUow
from src.resource.base import BaseResource
from src.services.admin.item import ItemService
from src.shared.exception.ledger_exception import LedgerException


class ItemResource(BaseResource):

    def get(self):
        item_service = ItemService()
        response = item_service.get_item(self.message_bus.uow)
        return response

    def post(self):
        try:
            data = request.get_json()
            item_service = ItemService()
            response = item_service.create_item(data, self.message_bus.uow)
            print(response)
            return response
        except LedgerException as ex:
            print(ex.code.value, ex.message.value)
            return {
                'error_code': ex.code.value,
                'error_message': ex.message.value
            }, 400
        except Exception as ex:
            return {
                'error_code': 111,
                'error_message': ex.args
            }, 500


class ItemDetailResource(BaseResource):

    def get(self, code):
        item_service = ItemService()
        response = item_service.get_item_by_code(code, self.message_bus.uow)
        return response

    def put(self, code):
        data = request.get_json()
        item_service = ItemService()
        response = item_service.update_item_by_code(code, data, self.message_bus.uow)
        return response

    def delete(self, code):
        item_service = ItemService()
        response = item_service.delete_item_by_code(code, self.message_bus.uow)
        return response
