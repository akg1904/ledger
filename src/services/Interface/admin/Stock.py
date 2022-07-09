import abc

from src.infrastructure.interface.sql_uow import SqlUow


class StockServiceInterface(abc.ABC):

    @abc.abstractmethod
    def get_stock_by_item_code(self, code: str, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def create_stock(self, data: dict, code: str, r_id: str, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def get_stock_by_id(self, ids: str, code: str,  uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def update_stock_by_id(self, ids: str, code: str, data: dict, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_stock_by_id(self, ids: str, code: str, uow: SqlUow):
        raise NotImplementedError

