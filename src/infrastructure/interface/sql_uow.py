
import abc

from sqlalchemy.orm import Session

from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class SqlUow(abc.ABC):

    def __init__(self):
        self._session: Session = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def get_session(self) -> Session:
        if not self._session:
            raise LedgerException(ErrorCode.INVALID_SESSION, ErrorMessage.INVALID_SESSION)
        return self._session

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

