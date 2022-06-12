from src.bootstrap.bus.message_bus import MessageBus
from src.database.interface.sql_uow import SqlUow
from src.database.uow.ledger_sql_uow import LedgerSqlUow


def bootstrap() -> MessageBus:
    uow: SqlUow = LedgerSqlUow()
    return MessageBus(
        uow
    )

