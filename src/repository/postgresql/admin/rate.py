from uuid import uuid4

from sqlalchemy.exc import SQLAlchemyError

from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.interface.rate import RateRepositoryInterface
from src.shared.exception.custom_exception import CustomException
from src.shared.exception.error_code import ErrorCode
from src.shared.exception.error_message import ErrorMessage
from src.shared.exception.ledger_exception import LedgerException


class RateRepository(RateRepositoryInterface):

    def __init__(self):
        # db_details = {
        #     'user_name': 'postgres',
        #     'password': 'root',
        #     'host': 'localhost',
        #     'port': '5432',
        #     'db_name': 'ledger'
        # }
        # self.engine = create_engine('postgresql://postgres:root@localhost:5432/ledger')
        # Below should be in get_rate
        # with Session(self.engine) as session:
        #     session: Session = session
        #     session.execute("""
        #
        #     """)
        #     session.commit()
        #     session.close()
        pass

    def get_rate_by_code(self, code: str, uow: SqlUow):
        try:
            results = list(uow.get_session().execute(
                """
                    Select item_code, CAST(id as Varchar) as id, p_rate, s_rate FROM rate 
                    WHERE 
                        item_code = :code
                """,
                dict(code=code)
            ))
            records = []
            for result in results:
                records.append({
                    "item_code": result['item_code'],
                    "id": result['id'],
                    "p_rate": result['p_rate'],
                    "s_rate": result['s_rate']
                })
            return records
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, ErrorMessage.SQL_ALCHEMY.value)
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_INSERTION_ERROR, ErrorMessage.RATE_INSERTION_ERROR)

    def create_rate(self, code: str, data: dict, uow: SqlUow):
        try:
            data['id'] = uuid4()
            uow.get_session().execute(
                """
                    Insert Into rate
                        (id, item_code, p_rate, s_rate)
                    Values
                        (:id, :code, :p_rate, :s_rate)            
                """,
                dict(id=data['id'], code=code, p_rate=data['p_rate'], s_rate=data['s_rate'])
            )
            return {"id": str(data['id']), "code": code, "p_rate": data['p_rate'], "s_rate": data['s_rate']}
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, ErrorMessage.SQL_ALCHEMY.value)
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_INSERTION_ERROR, ErrorMessage.RATE_INSERTION_ERROR)

    def get_rate_by_id(self, ids: str, code: str, uow: SqlUow):
        try:
            result = uow.get_session().execute(
                """
                    select CAST(item_code as Varchar) as item_code, CAST(id as Varchar) as id, p_rate, s_rate FROM rate
                    WHERE
                        id = :id and item_code = :code
                """,
                dict(id=ids, code=code)
            ).first()
            if result:
                return dict(result)
            return None
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, ErrorMessage.SQL_ALCHEMY.value)
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_INSERTION_ERROR, ErrorMessage.RATE_INSERTION_ERROR)

    def update_rate_by_id(self, ids: str, data: dict, uow: SqlUow):
        try:
            uow.get_session().execute(
                """
                    Update rate Set p_rate = :p_rate, s_rate = :s_rate
                    WHERE id = :id
                """,
                dict(id=ids, p_rate=data['p_rate'], s_rate=data['s_rate'])
            )
            return ids
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, ErrorMessage.SQL_ALCHEMY.value)
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_INSERTION_ERROR, ErrorMessage.RATE_INSERTION_ERROR)

    def delete_rate_by_id(self, ids: str, uow: SqlUow):
        try:
            uow.get_session().execute(
                """
                    Delete FROM rate WHERE id = :id
                """,
                dict(id=ids)
            )
        except SQLAlchemyError as ex:
            raise CustomException(ErrorCode.SQL_ALCHEMY.value, ErrorMessage.SQL_ALCHEMY.value)
        except Exception as ex:
            raise LedgerException(ErrorCode.RATE_DELETING_ERROR, ErrorMessage.RATE_DELETING_ERROR)

