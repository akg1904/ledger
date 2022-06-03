from src.database.interface.sql_uow import SqlUow
from src.database.uow.ledger_sql_uow import LedgerSqlUow


def bootstrap() -> SqlUow:
    uow: SqlUow = LedgerSqlUow()
    return uow