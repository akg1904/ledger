from app import app
from src.database.interface.sql import Sql


DEFAULT_SESSION_FACTORY = app.config['DB_SESSION']


class LedgerSql(Sql):

    def __int__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
