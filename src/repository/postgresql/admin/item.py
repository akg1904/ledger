from typing import List, Dict

from sqlalchemy.exc import SQLAlchemyError

from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.interface.item import ItemInterface
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class ItemRepository(ItemInterface):

    def create_item(self, data: dict, uow: SqlUow) -> str:
        try:
            uow.get_session().execute(
                """
                    insert into items 
                        (code, name, description)
                    values
                        (:code, :name, :desc)
                """,
                dict(code=data['code'], name=data['name'], desc=data['desc'])
            )
            return data['code']

        except SQLAlchemyError as ex:
            print("SqlAlchemy error: ", ex)
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, str(ex))
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            print("Exception error: ", ex)
            raise LedgerException(ErrorCode.ITEM_NOT_CREATED, ErrorMessage.ITEM_NOT_CREATED)

    def get_items(self, uow: SqlUow) -> List[Dict]:
        try:
            result = list(uow.get_session().execute(
                """
                    select code, name, description from items
                """
            ))
            items = []
            if result:
                for item in result:
                    items.append(dict(item))
            return items

        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, str(ex))
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_FETCH_ERROR, ErrorMessage.ITEM_FETCH_ERROR)

    def get_item_by_code(self, code: str, uow: SqlUow):
        print(code)
        try:
            result = uow.get_session().execute(
                """
                    select name, description from items
                    where code = (:code)
                """,
                dict(code=code)
            ).first()
            if result:
                return dict(result)

            return None
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, str(ex))
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_FETCH_ERROR, ErrorMessage.ITEM_FETCH_ERROR)

    def update_item_by_code(self, code: str, data: dict, uow: SqlUow):
        try:
            uow.get_session().execute(
                """
                    Update items set name = :name where code= :code                   
                """,
                dict(code=code, name=data['name'])
            )
            return code
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, str(ex.args))
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_UPDATING_ERROR, ErrorMessage.ITEM_UPDATING_ERROR)

    def delete_item_by_code(self, code: str, uow: SqlUow):
        try:
            uow.get_session().execute(
                """
                    Delete from items where code = :code
                """,
                dict(code=code)
            )
            return code
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, ErrorMessage.SQL_ALCHEMY.value)
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.ITEM_DELETING_ERROR, ErrorMessage.ITEM_DELETING_ERROR)

