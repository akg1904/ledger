

from sqlalchemy import *
from migrate import *

metadata = MetaData()

items = Table(
    "items", metadata,
    Column('i_code', String(5), primary_key=True, nullable=False),
    Column('i_name', String(50), nullable=False),
    Column('description', String(50), nullable=False)
)



def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata.bind = migrate_engine
    items.create()



def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata.bind = migrate_engine
    items.drop()


