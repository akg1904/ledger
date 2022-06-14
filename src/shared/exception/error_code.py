from enum import Enum


class ErrorCode(Enum):

    SUCCESS = 2000
    FAILURE = 4000
    USER_EXISTS = 2010
    USER_CREATION_FAILED = 2011
