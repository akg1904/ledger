from sqlalchemy import MetaData, Table
from migrate import ForeignKeyConstraint


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata = MetaData(bind=migrate_engine)
    item = Table("items", metadata, autoload=True)
    rate = Table("rate", metadata, autoload=True)
    ForeignKeyConstraint([rate.c.item_code], [item.c.code]).create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata = MetaData(bind=migrate_engine)
    item = Table("items", metadata, autoload=True)
    rate = Table("rate", metadata, autoload=True)
    ForeignKeyConstraint([rate.c.item_code], [item.c.code]).drop()

