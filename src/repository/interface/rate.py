import abc

from src.infrastructure.interface.sql_uow import SqlUow


class RateRepositoryInterface(abc.ABC):

    @abc.abstractmethod
    def get_rate_by_code(self, code: str, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def create_rate(self, code: str, data: dict, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def get_rate_by_id(self, ids: str, code: str, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def update_rate_by_id(self, ids: str, data: dict, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_rate_by_id(self, ids: str, uow: SqlUow):
        raise NotImplementedError
