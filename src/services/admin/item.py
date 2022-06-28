from src.database.interface.sql_uow import SqlUow
from src.repository.postgresql.admin.item import ItemRepository
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class ItemService:

    def __init__(self):
        self.item_repository = ItemRepository()

    def create_item(self, data, uow: SqlUow):
        item = None
        with uow:
            item = self.item_repository.get_item_by_code(data["code"], uow)
            if item:
                raise LedgerException(ErrorCode.ITEM_ALREADY_EXISTS, ErrorMessage.ITEM_ALREADY_EXISTS)
            self.item_repository.create_item(data, uow)
            uow.commit()

        with uow:
            created_item = self.item_repository.get_item_by_code(data["code"], uow)
            if not created_item:
                raise LedgerException(ErrorCode.ITEM_NOT_CREATED, ErrorMessage.ITEM_NOT_CREATED)

        return created_item

    def get_item(self, uow: SqlUow):
        items = []
        with uow:
            items = self.item_repository.get_items(uow)
        return items

    def get_item_by_code(self, code, uow: SqlUow):
        with uow:
            item = self.item_repository.get_item_by_code(code, uow)
        return item

    def update_item_by_code(self, code, data, uow: SqlUow):
        item = None
        with uow:
            self.item_repository.update_item_by_code(code, data, uow)
            uow.commit()
            item = self.item_repository.get_item_by_code(code, uow)
        return item

    def delete_item_by_code(self, code, uow:SqlUow):
        item = None
        with uow:
            self.item_repository.delete_item_by_code(code, uow)
            uow.commit()
            item = self.item_repository.get_items(uow)
        return item
