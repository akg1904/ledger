import uuid

from src.repository.interface.user import UserInterface


class UserSqlite(UserInterface):

    def create_user(self, data, uow):
        id = uuid.uuid4()
        emp_id = "E-001"
        user_name = "test123"
        password = "welcome123"
        tenant_id = "TEST01"

        uow.session.execute(
            """
            INSERT INTO login_details 
                (id, emp_id, username, password, active, tenant_id)
                VALUES
                (:id, :emp_id, :user_name, :password, 'true', :tenant_id) 
            """,
            dict(id=id, emp_id=emp_id, user_name=user_name, password=password, tenant_id=tenant_id)
        )


    def delete_user_by_id(self, id):
        pass

    def update_user_by_id(self, id):
        pass

    def get_user_by_id(self, id):
        pass

    def get_all_user(self):
        pass