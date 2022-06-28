
from src.database.entity.tables import ItemEntity
from src.database.interface.sql_uow import SqlUow
from src.repository.interface.item import ItemInterface
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class ItemRepository(ItemInterface):

    def __init__(self):
        pass

    def create_item(self, data: dict, uow: SqlUow):
        # item = ItemEntity(
        #     code = data['code'],
        #     name = data['name'],
        #     desc = data['desc']
        # )
        # uow.session.add(item)
        try:
            uow.session.execute(
                """
                    INSERT INTO items 
                    (code, name, description)
                     VALUES 
                     (:code, :name, :desc);
                """,
                dict(code = data['code'], name= data['name'], desc= data['desc'])
            )
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_CREATION_FAILED, ErrorMessage.ITEM_CREATION_FAILED)

    def get_items(self, uow: SqlUow):
        try:
            result = list(uow.session.execute(
                """
                SELECT code, name, description 
                FROM items
                """
            ))
            if result:
                items = []
                for item in result:
                    temp = {
                        'code': item.code,
                        'name': item.name,
                        'desc': item.description
                    }
                    items.append(temp)

                return items
        except Exception as ex:
            print(ex)

    def get_item_by_code(self, code, uow: SqlUow):
        try:
            item = None
            result = uow.session.execute(
                """
                SELECT code, name, description
                FROM items
                WHERE code = :code
                """,
                dict(code=code)
            ).first()
            if result:
                item = {
                    'code': result.code,
                    'name': result.name,
                    'desc': result.description
                }
            return item
        except Exception as ex:
            print(ex)

    def update_item_by_code(self, code: str, data: dict, uow: SqlUow):
        try:
            uow.session.execute(
                """
                UPDATE items
                SET
                    name = :name
                WHERE code = :code
                """,
                dict(name=data['name'], code=code)
            )
        except Exception as ex:
            print(ex)

    def delete_item_by_code(self, code, uow: SqlUow):
        try:
            uow.session.execute(
                """
                DELETE From items
                WHERE code = :code
                """,
                dict(code=code)
            )
        except Exception as ex:
            print(ex)



