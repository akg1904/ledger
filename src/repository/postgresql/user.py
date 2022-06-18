import uuid

from sqlalchemy.exc import SQLAlchemyError

from src.database.entity.tables import UserEntity
from src.database.interface.sql_uow import SqlUow
from src.repository.interface.user import UserInterface
from src.shared.exception.ledger_exception import LedgerException


class UserPostRepository(UserInterface):

    def __init__(self):
        pass

    def create_user(self, data: dict, uow: SqlUow):
        try:
            user = UserEntity(
                id = uuid.uuid4(),
                emp_id = data['emp_id'],
                username = data['user_name'],
                password = data['password'],
                active=True,
                tenant_id = data['tenant_id']
            )
            uow.session.add(user)
            return data['emp_id']
        except SQLAlchemyError as ex:
            print(ex)
            raise LedgerException()

        # uow.session.execute(
        #     """
        #     INSERT INTO login_details
        #         (id, emp_id, username, password, active, tenant_id)
        #     VALUES
        #         (:id, :emp_id, :user_name, :password, 'true', :tenant_id)
        #     """,
        #     dict(id=id, emp_id=emp_id, user_name=user_name, password=password, tenant_id=tenant_id)
        # )

    def delete_user_by_id(self, emp_id, uow: SqlUow):
        uow.session.execute(
            """
            DELETE FROM user_details
            WHERE emp_id = :emp_id""",
            dict(emp_id=emp_id)
        )
        return {"msg": "Record Deleted"}

    def update_user_by_emp_id(self, emp_id, uow: SqlUow):
        uow.session.execute(
            """
            UPDATE user_details
            SET
                username = 'Abhishek'
            WHERE emp_id = :emp_id""",
            dict(emp_id=emp_id)
        )
        return {"msg": "Record Updated"}

    def get_user_by_emp_id(self, emp_id, uow: SqlUow):

        response = uow.session.execute(
            """
            SELECT CAST(id as VARCHAR) as id, emp_id, username, tenant_id
            FROM user_details
            WHERE emp_id = :emp_id""",
            dict(emp_id = emp_id)
        ).first()
        user = {
            'id': response.id,
            'emp_id': response.emp_id,
            'user_name': response.username,
            'tenant_id': response.tenant_id
        }
        return user

    def get_user_by_username(self, username, uow: SqlUow):
        user = None
        response = uow.session.execute(
                        """
                        SELECT CAST(id as VARCHAR) as id, emp_id, username, tenant_id 
                        FROM user_details 
                        WHERE username = :user_name
                        """,
                        dict(user_name = username)
                    ).first()
        if response is not None:
            user = {
                'id': response.id,
                'emp_id': response.emp_id,
                'user_name': response.username,
                'tenant_id': response.tenant_id
            }
        return user

    def get_all_user(self, uow: SqlUow):
        result_set = list(uow.session.execute(
            """
            SELECT CAST(id as VARCHAR) as id, emp_id, username, password, tenant_id 
            FROM user_details 
            """
        ))

        users = []

        for user in result_set:
            temp = {
                'id' : user.id,
                'emp_id': user.emp_id,
                'user_name': user.username,
                'tenant_id': user.tenant_id
            }
            users.append(temp)

        return users

    def update_user_by_id(self, id):
        pass
