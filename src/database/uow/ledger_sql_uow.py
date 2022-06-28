from sqlalchemy.orm import sessionmaker, Session

from src.database.db.postgresql import PostgresDB
from src.database.interface.sql_uow import SqlUow


# DEFAULT_SESSION_FACTORY = app.config['DB_SESSION']


class LedgerSqlUow(SqlUow):
    """
    Ledger Unit of Work
    """

    def __init__(self, session_factory=None):
        DB_Engine = PostgresDB().get_connection()
        session_factory = sessionmaker(bind=DB_Engine)
        self.session_factory = session_factory

    def __enter__(self):
        self.session: Session = self.session_factory()
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
