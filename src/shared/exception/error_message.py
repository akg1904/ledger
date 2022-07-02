from enum import Enum


class ErrorMessage(Enum):

    SUCCESS = "Code Success"
    FAILURE = "Api failed"
    INVALID_SESSION = "Invalid Session"
    SQL_ALCHEMY = "Sql Alchemy exception"
    USER_EXISTS = 'User already exists'
    USER_CREATION_FAILED = 'Failed to create user'
    ITEM_CREATION_FAILED = 'Failed to create item'
    ITEM_NOT_CREATED = 'Item not created'
    ITEM_ALREADY_EXISTS = 'Item already present'
    ITEM_FETCH_ERROR = 'Item fetching failed'
    ITEM_UPDATING_ERROR = 'Item Updating failed'
    ITEM_DELETING_ERROR = 'Item Deleting failed'
    ITEM_NOT_FOUND = 'Item not found'






