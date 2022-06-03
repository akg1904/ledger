from uuid import UUID, uuid4

from sqlalchemy import MetaData, Table, Column, String, Boolean

metadata = MetaData()

login = Table(
    "login_details", metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4(), nullable=False),
    Column('emp_id', String(10), nullable=False),
    Column('username', String(50), unique=True, nullable=False),
    Column('password', String(50), unique=True, nullable=False),
    Column('active', Boolean, nullable=False),
    Column('tenant_id', String(20), nullable=False)
)
