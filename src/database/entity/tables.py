import uuid
from uuid import uuid4

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID

# metadata = MetaData()
# TenantBase = declarative_base(name="TenantBase")
#
# login = Table(
#     "login_details", TenantBase.metadata,
#     Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4(), nullable=False),
#     Column('emp_id', String(10), nullable=False),
#     Column('username', String(50), unique=True, nullable=False),
#     Column('password', String(50), unique=True, nullable=False),
#     Column('active', Boolean, nullable=False),
#     Column('tenant_id', String(20), nullable=False)
# )

GlobalBase = declarative_base(name="GlobalBase")
TenantBase = declarative_base(name="TenantBase")


class UserEntity(TenantBase):
    __tablename__ = "login_details"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4(), nullable=False)
    emp_id = Column( String(10), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=True, nullable=False)
    active = Column(Boolean, nullable=False)
    tenant_id = Column(String(20), nullable=False)

    def __init__(
            self,
            emp_id: str,
            username: str,
            password: str,
            tenant_id: str,
            id: UUID = uuid.uuid4(),
            active: bool = True
    ):
        self.id = id
        self.emp_id = emp_id
        self.username = username
        self.password = password
        self.active = active
        self.tenant_id = tenant_id







