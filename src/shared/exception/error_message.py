from enum import Enum


class ErrorMessage(Enum):

    SUCCESS = "Code Success"
    FAILURE = "Api failed"
    USER_EXISTS = 'User already exists'
    USER_CREATION_FAILED = 'Failed to create user'
    ITEM_CREATION_FAILED = 'Failed to create item'
    ITEM_NOT_CREATED = 'Item not created'
    ITEM_ALREADY_EXISTS = 'Item already present'






