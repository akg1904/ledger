import abc
from typing import List, Dict

from src.infrastructure.interface.sql_uow import SqlUow


class ItemInterface(abc.ABC):

    @abc.abstractmethod
    def create_item(self, data: dict, uow: SqlUow) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_items(self, uow: SqlUow) -> List[Dict]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_item_by_code(self, code: str, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def update_item_by_code(self, code: str, name: str, uow: SqlUow):
        raise NotImplementedError

    @abc.abstractmethod
    def delete_item_by_code(self, code:str, uow: SqlUow):
        raise NotImplementedError

