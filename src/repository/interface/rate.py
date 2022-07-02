import abc

from src.infrastructure.interface.sql_uow import SqlUow


class RateInterface(abc.ABC):

    @abc.abstractmethod
    def get_rate(self, uow: SqlUow):
        raise NotImplementedError

