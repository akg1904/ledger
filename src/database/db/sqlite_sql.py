import sqlite3

from src.database.interface.database import Database


class Sqlite(Database):
    __instance = None

    def __int__(self):
        super().__init__()
        self.conn = sqlite3.connect('src/database/ledger.db')
        print("Database Connected: ")
        Sqlite.__instance = self.conn

    def get_connection(self):
        if Sqlite.__instance is None:
            Sqlite()
        return Sqlite.__instance

