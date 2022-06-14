from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage


class LedgerException(Exception):

    def __init__(self, code: ErrorCode, message: ErrorMessage):
        self.code: ErrorCode = code
        self.message: ErrorMessage = message
