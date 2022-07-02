from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.interface.rate import RateInterface


class RateRepository(RateInterface):

    def __init__(self):
        db_details = {
            'user_name': 'postgres',
            'password': 'root',
            'host': 'localhost',
            'port': '5432',
            'db_name': 'ledger'
        }
        self.engine = create_engine('postgresql://postgres:root@localhost:5432/ledger')

    def get_rate(self, uow: SqlUow):
        with Session(self.engine) as session:
            session: Session = session
            session.execute("""
            
            """)
            session.commit()
            session.close()


