from sqlalchemy import create_engine

from src.database.interface.database import Database


class PostgresDB(Database):

    __instance = None

    def __init__(self, **kwargs):
        super().__init__()

        db_details = {
            'user_name': 'postgres',
            'password': 'root',
            'host': 'localhost',
            'port': '5432',
            'db_name': 'ledger'
        }
        self.__engine = create_engine(
            'postgresql://{}:{}@{}:{}/{}'.format(
                db_details['user_name'],
                db_details['password'],
                db_details['host'],
                db_details['port'],
                db_details['db_name'],
            )
        )
        PostgresDB.__instance = self.__engine

    def get_connection(self):
        if PostgresDB.__instance is None:
            PostgresDB()
        return PostgresDB.__instance
