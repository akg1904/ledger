from redis.client import Redis

from src.infrastructure.interface.database import Database


class RedisKVStore(Database):

    __instance: Redis = None

    def __init__(self, **kwargs):
        super().__init__()

        db_details = {
            'host': 'localhost',
            'port': 6379
        }
        redis: Redis = Redis(host=db_details['host'], port=db_details['port'])
        RedisKVStore.__instance = redis

    def get_connection(self, **kwargs):
        if RedisKVStore.__instance is None:
            RedisKVStore(**kwargs)
        return RedisKVStore.__instance
