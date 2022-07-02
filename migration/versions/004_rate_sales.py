from sqlalchemy import MetaData, Table, Column, String, Integer, Date, Float, FLOAT
from migrate import *
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

rate_sales = Table(
    "rate", metadata,
    Column("id", String(10), primary_key=True, nullable=False),
    Column("item_code", String(5), nullable=False),
    Column("p_rate", Float(9), nullable=False),
    Column("s_rate", Float(9), nullable=False)
)

stock = Table(
    "stock", metadata,
    Column("id", String(10), primary_key=True, nullable=False),
    Column("item_code", String(10), nullable=False),
    Column("r_id", String(10), nullable=False),
    Column("qty", Integer, nullable=False)
)

supplier = Table(
    "supplier", metadata,
    Column("id", Integer, primary_key=True, nullable=False, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("addr", String(50), nullable=True),
    Column("city", String(20), nullable=True),
    Column("state", String(20), nullable=True),
    Column("country", String(20), nullable=True),
    Column("pincode", Integer, nullable=True),
    Column("contact_no", Integer, nullable=True),
    Column("gst", String(20), nullable=True)
)

customer = Table(
    "customer", metadata,
    Column("id", Integer, primary_key=True, nullable=False, autoincrement=True),
    Column("name", String(50), nullable=False),
    Column("addr", String(50), nullable=True),
    Column("city", String(20), nullable=True),
    Column("state", String(20), nullable=True),
    Column("country", String(20), nullable=True),
    Column("pincode", Integer, nullable=True),
    Column("contact_no", Integer, nullable=True)
)

purchase = Table(
    "purchase", metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
    Column("su_id", Integer, nullable=False),
    Column("bill_no", String(10), nullable=False),
    Column("date", Date, nullable=False),
    Column("amount", Float(11), nullable=False)
)


purchase_detail = Table(
    "purchase_details", metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
    Column("p_id", UUID(as_uuid=True), nullable=False),
    Column("item_code", String(10), nullable=False),
    Column("rate", Float(9), nullable=False),
    Column("qty", Float(11), nullable=False)
)

# sales = Table(
#     "sales", metadata,
#     Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
#     Column("su_id", Integer, nullable=False),
#     Column("bill_no", String(10), nullable=False),
#     Column("date", Date, nullable=False),
#     Column("amount", Float(11), nullable=False)
# )
#
# sales_details = Table(
#     "sales_details", metadata,
#     Column("id", UUID(as_uuid=True), primary_key=True, nullable=False),
#     Column("s_id", UUID(as_uuid=True), nullable=False),
#     Column("item_code", String(10), nullable=False),
#     Column("rate", Float(9), nullable=False),
#     Column("qty", Float(11), nullable=False)
# )


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata.bind = migrate_engine
    rate_sales.create()
    stock.create()
    supplier.create()
    customer.create()
    purchase.create()
    purchase_detail.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata.bind = migrate_engine
    rate_sales.drop()
    stock.drop()
    supplier.drop()
    customer.drop()
    purchase.drop()
    purchase_detail.drop()

