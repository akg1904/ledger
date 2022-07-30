import json
import uuid
from datetime import timedelta

from redis.client import Redis

from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.postgresql.auth.user import UserPostRepository
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class LoginService:

    def __init__(self):
        self.userRepository = UserPostRepository()

    def validate_user(self, data: dict, uow: SqlUow, redis: Redis):
        with uow:
            user = self.userRepository.get_user_by_username(data['username'], uow)
            if not user:
                raise LedgerException(ErrorCode.USER_NOT_FOUND, ErrorMessage.USER_NOT_FOUND)

            if user['password'] != data['password']:
                raise LedgerException(ErrorCode.INVALID_PASSWORD, ErrorMessage.INVALID_PASSWORD)

            del user['password']
            token, token_key = self._generate_token()
            redis.setex(token_key, timedelta(minutes=int(60)), json.dumps(user))
            return token

    def _generate_token(self):

        token = uuid.uuid4().hex
        token_key = "ledger_" + token
        return token, token_key







