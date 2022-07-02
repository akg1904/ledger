import uuid

from src.repository.interface.user import UserInterface


class UserSqlite(UserInterface):

    def create_user(self, data: dict, uow):
        id = uuid.uuid4()
        data['id'] = str(id)
        emp_id = data['emp_id']
        user_name = data['user_name']
        password = data['password']
        tenant_id = data['tenant_id']

        uow._session.execute(
            """
            INSERT INTO login_details 
                (id, emp_id, username, password, active, tenant_id)
                VALUES
                    (:id, :emp_id, :user_name, :password, 'true', :tenant_id) 
            """,
            dict(id=id, emp_id=emp_id, user_name=user_name, password=password, tenant_id=tenant_id)
        )
        return data

    def delete_user_by_id(self, id):
        pass

    def update_user_by_id(self, id):
        pass

    def get_user_by_username(self, username):

        response = username(
            """
            SELECT * FROM login_details 
                WHERE user_name = 'test1'
            """
        )
        return response

    def get_all_user(self):
        pass