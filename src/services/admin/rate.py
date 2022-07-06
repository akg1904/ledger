from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.interface.rate import RateRepositoryInterface
from src.repository.postgresql.admin.item import ItemRepository
from src.repository.postgresql.admin.rate import RateRepository
from src.services.Interface.admin.rate import RateServiceInterface
from src.services.admin.item import ItemService
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class RateService(RateServiceInterface):

    def __init__(self):
        self.rate_repository: RateRepositoryInterface = RateRepository()
        # self.item_repository = ItemRepository()
        self.item_service = ItemService()

    def get_rate_by_item_code(self, code: str, uow: SqlUow):
        try:
            with uow:
                response = self.rate_repository.get_rate_by_code(code, uow)
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_FETCHING_ERROR, ErrorMessage.RATE_FETCHING_ERROR)

    def create_rate(self, data: dict, code: str, uow: SqlUow):
        try:
            _ = self.item_service.get_item_by_code(code, uow)
            with uow:
                response = self.rate_repository.create_rate(code, data, uow)
                uow.commit()
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_INSERTION_ERROR, ErrorMessage.RATE_INSERTION_ERROR)

    def get_rate_by_id(self, ids: str, code: str, uow: SqlUow):
        try:
            with uow:
                response = self.rate_repository.get_rate_by_id(ids, code, uow)
                if not response:
                    raise LedgerException(ErrorCode.RATE_RECORD_NOT_FOUND, ErrorMessage.RATE_RECORD_NOT_FOUND)
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_FETCHING_ERROR, ErrorMessage.RATE_FETCHING_ERROR)

    def update_rate_by_id(self, ids: str, code: str, data: dict, uow: SqlUow):
        try:
            with uow:
                get_by_id = self.rate_repository.get_rate_by_id(ids, code, uow)
                if not get_by_id:
                    raise LedgerException(ErrorCode.ITEM_NOT_FOUND, ErrorMessage.ITEM_NOT_FOUND)
                response = self.rate_repository.update_rate_by_id(ids, data, uow)
                uow.commit()
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_UPDATING_ERROR, ErrorMessage.RATE_UPDATING_ERROR)

    def delete_rate_by_id(self, ids: str, uow: SqlUow):
        try:
            with uow:
                response = self.rate_repository.delete_rate_by_id(ids, uow)
                uow.commit()
                return response
        except CustomException as ex:
            raise ex
        except LedgerException as ex:
            raise ex
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_DELETING_ERROR, ErrorMessage.RATE_DELETING_ERROR)

