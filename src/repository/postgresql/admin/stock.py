from uuid import uuid4

from sqlalchemy.exc import SQLAlchemyError

from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.interface.stock import StockRepositoryInterface
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class StockRepository(StockRepositoryInterface):

    def get_stock_by_item_code(self, code: str, uow: SqlUow):
        return {"msg": "stock repository"}

    def create_stock(self, data: dict, code: str, r_id: str, uow: SqlUow):
        try:
            data['id'] = uuid4()
            uow.get_session().execute(
                """
                    Insert into stock (id, item_code, r_id, qty) Values (:id, :code, :r_id, :qty)                    
                """,
                dict(id=data['id'], code=code, r_id=r_id, qty=data['qty'])
            )
            return {"id": str(data['id']), "code": code, "r-id": r_id, "qty": data['qty']}
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, ErrorMessage.SQL_ALCHEMY.value)
        except Exception as ex:
            raise LedgerException(ErrorCode.STOCK_INSERTION_ERROR, ErrorMessage.STOCK_INSERTION_ERROR)

    def get_stock_by_id(self, ids: str, code: str, uow: SqlUow):
        pass

    def update_stock_by_id(self, ids: str, code: str, data: dict, uow: SqlUow):
        pass

    def delete_stock_by_id(self, ids: str, code: str, uow: SqlUow):
        pass
