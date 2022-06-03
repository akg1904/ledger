from app import app
from src.database.interface.sql_uow import SqlUow


DEFAULT_SESSION_FACTORY = app.config['DB_SESSION']


class LedgerSqlUow(SqlUow):
    """
    Ledger Unit of Work
    """

    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
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

# app.config['DB_INSTANCE'] = PostgresDB().get_connection()
# app.config['DB_SESSION'] = sessionmaker(bind=app.config['DB_INSTANCE'])
# DEFAULT_SESSION_FACTORY = app.config['DB_SESSION']
# session_factory = DEFAULT_SESSION_FACTORY
# connection = session_factory()
# connection.add('hello')
# connection.commit()
# connection.close()
#
#
# session = LedgerSqlUow()
# with session as uow:
#     uow.add('hello')
#     uow.commit()
