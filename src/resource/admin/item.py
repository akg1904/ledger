

from flask import request


from src.resource.base import BaseResource
from src.services.admin.item import ItemService
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.ledger_exception import LedgerException
from src.shared.response.response_data import response_payload

item_service: ItemService = ItemService()


class ItemResource(BaseResource):

    def get(self):

        try:
            items = item_service.get_items(self.message_bus.uow)
            return response_payload(items, "got items", 2000, True), 200
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 401
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 5000, False), 500

    def post(self):
        try:
            data = request.get_json()
            response = item_service.create_item(data, self.message_bus.uow)
            return response_payload(response, "Item Created"), 201
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 5000, False), 500


class ItemDetailResource(BaseResource):


    def get(self, **kwargs):
        try:
            item = item_service.get_item_by_code(kwargs['code'], self.message_bus.uow)
            return response_payload(item, "item received"), 200
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 5000, False), 500

    def put(self, **kwargs):
        try:
            data = request.get_json()
            response = item_service.update_item_by_code(kwargs['code'], data, self.message_bus.uow)
            return response_payload(response, "Item Updated"), 200
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 5000, False), 500

    def delete(self, **kwargs):
        try:
            response = item_service.delete_item_by_code(kwargs['code'], self.message_bus.uow)
            return response_payload(response, "Record Deleted"), 200
        except CustomException as ex:
            return response_payload(None, ex.message, ex.code, False), 400
        except LedgerException as ex:
            return response_payload(None, ex.message.value, ex.code.value, False), 400
        except Exception as ex:
            return response_payload(None, ex.args, 5000, False), 500
