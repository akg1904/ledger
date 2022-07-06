from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.interface.item import ItemInterface
from src.repository.postgresql.admin.item import ItemRepository
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class ItemService:

    def __init__(self):
        self.item_repository: ItemInterface = ItemRepository()

    def create_item(self, data: dict, uow: SqlUow) -> str:
        try:
            with uow:
                item = self.item_repository.get_item_by_code(data['code'], uow)
                if item:
                    raise LedgerException(ErrorCode.ITEM_ALREADY_EXISTS, ErrorMessage.ITEM_ALREADY_EXISTS)
                response = self.item_repository.create_item(data, uow)
                uow.commit()
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_NOT_CREATED, ErrorMessage.ITEM_NOT_CREATED)

    def get_items(self, uow: SqlUow):
        try:
            with uow:
                items = self.item_repository.get_items(uow)
            return items
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_FETCH_ERROR, ErrorMessage.ITEM_FETCH_ERROR)

    def get_item_by_code(self, code, uow: SqlUow):
        try:
            with uow:
                item = self.item_repository.get_item_by_code(code, uow)
                if not item:
                    raise LedgerException(ErrorCode.ITEM_NOT_FOUND, ErrorMessage.ITEM_NOT_FOUND)
                return item
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_FETCH_ERROR, ErrorMessage.ITEM_FETCH_ERROR)

    def update_item_by_code(self, code: str, data: dict, uow: SqlUow):
        try:
            with uow:
                item = self.item_repository.get_item_by_code(code, uow)
                if not item:
                    raise LedgerException(ErrorCode.ITEM_NOT_FOUND, ErrorMessage.ITEM_NOT_FOUND)
                response = self.item_repository.update_item_by_code(code, data, uow)
                uow.commit()
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_UPDATING_ERROR, ErrorMessage.ITEM_UPDATING_ERROR)

    def delete_item_by_code(self, code: str, uow: SqlUow):
        try:
            with uow:
                item = self.item_repository.get_item_by_code(code, uow)
                if not item:
                    raise LedgerException(ErrorCode.ITEM_ALREADY_DELETED, ErrorMessage.ITEM_ALREADY_DELETED)
                response = self.item_repository.delete_item_by_code(code, uow)
                uow.commit()
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_DELETING_ERROR, ErrorMessage.ITEM_DELETING_ERROR)


