from redis.client import Redis

from src.bootstrap.bus.message_bus import MessageBus
from src.infrastructure.db.redis import RedisKVStore
from src.infrastructure.interface.sql_uow import SqlUow
from src.infrastructure.uow.ledger_sql_uow import LedgerSqlUow


def bootstrap() -> MessageBus:
    uow: SqlUow = LedgerSqlUow()
    redis: Redis = RedisKVStore().get_connection()

    return MessageBus(
        uow, redis
    )

