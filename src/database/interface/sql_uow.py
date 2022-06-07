
import abc

from sqlalchemy.orm import Session


class SqlUow(abc.ABC):

    def __init__(self):
        self.session: Session = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

