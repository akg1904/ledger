from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.postgresql.admin.stock import StockRepository
from src.services.Interface.admin.Stock import StockServiceInterface
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class StockService(StockServiceInterface):

    def __init__(self):
        self.stock_repository = StockRepository()

    def get_stock_by_item_code(self, code: str, uow: SqlUow):
        try:
            response = self.stock_repository.get_stock_by_item_code(code, uow)
            return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_FETCHING_ERROR, ErrorMessage.RATE_FETCHING_ERROR)

    def create_stock(self, data: dict, code: str, r_id: str, uow: SqlUow):
        try:
            with uow:
                response = self.stock_repository.create_stock(data, code, r_id, uow)
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.STOCK_INSERTION_ERROR, ErrorMessage.STOCK_INSERTION_ERROR)

    def get_stock_by_id(self, ids: str, code: str, uow: SqlUow):
        try:
            response = self.stock_repository.get_stock_by_id(ids, code, uow)
            return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_FETCHING_ERROR, ErrorMessage.RATE_FETCHING_ERROR)

    def update_stock_by_id(self, ids: str, code: str, data: dict, uow: SqlUow):
        try:
            response = self.stock_repository.update_stock_by_id(ids, code, data, uow)
            return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_FETCHING_ERROR, ErrorMessage.RATE_FETCHING_ERROR)

    def delete_stock_by_id(self, ids: str, code: str, uow: SqlUow):
        try:
            response = self.stock_repository.delete_stock_by_id(ids, code, uow)
            return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_FETCHING_ERROR, ErrorMessage.RATE_FETCHING_ERROR)

