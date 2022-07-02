from src.infrastructure.interface.sql_uow import SqlUow


class MessageBus:

    def __init__(self, uow: SqlUow):
        self.uow: SqlUow = uow
