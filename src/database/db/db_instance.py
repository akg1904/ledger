from src.database.db.sqlite_sql import Sqlite
from src.database.interface.database import Database


class DBInstance:

    def __init__(self, db_name='sqlite'):
        if db_name == 'sqlite':
            db_obj: Database = self.sqlite_obj()
        elif db_name == 'mysql':
            db_obj: Database = self.mysql_obj()
        # else:
        #     self.db = Sqlite().get_connection()

        self.db = self._get_connection(db_obj)

    def _get_connection(self, conn: Database):
        return conn.get_connection()

    def sqlite_obj(self):
        return Sqlite()

    def mysql_obj(self):
        return Sqlite()
