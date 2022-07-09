from redis.client import Redis

from src.infrastructure.interface.sql_uow import SqlUow


class MessageBus:

    def __init__(self, uow: SqlUow, redis: Redis):
        self.uow: SqlUow = uow
        self.redis: Redis = redis
