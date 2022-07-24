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
        try:
            result_set = list(uow.get_session().execute(
                """
                    SELECT CAST(id as Varchar) as id, item_code, CAST(r_id as Varchar) as r_id, qty 
                    FROM stock 
                    WHERE item_code = :code                    
                """,
                dict(code=code)
            ))
            stock = []
            if result_set:
                for result in result_set:
                    temp = {
                        'id': result['id'],
                        'item_code': result['item_code'],
                        'r_id': result['r_id'],
                        'qty': result['qty']
                    }
                    stock.append(temp)
                return stock
            return stock

        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, ErrorMessage.SQL_ALCHEMY.value)
        except Exception as ex:
            raise LedgerException(ErrorCode.STOCK_FETCHING_ERROR, ErrorMessage.STOCK_FETCHING_ERROR)

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
