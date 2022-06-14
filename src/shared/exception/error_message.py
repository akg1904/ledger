from enum import Enum


class ErrorMessage(Enum):

    SUCCESS = "Code Success"
    FAILURE = "Api failed"
    USER_EXISTS = 'User already exists'
    USER_CREATION_FAILED = 'Failed to create user'
