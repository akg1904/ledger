from sqlalchemy import MetaData, Table
from migrate import ForeignKeyConstraint


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata = MetaData(bind=migrate_engine)
    item = Table("items", metadata, autoload=True)
    rate = Table("rate", metadata, autoload=True)
    stock = Table("stock", metadata, autoload=True)
    ForeignKeyConstraint([rate.c.item_code], [item.c.code], onupdate="CASCADE", ondelete="CASCADE").create()
    ForeignKeyConstraint([stock.c.item_code], [item.c.code], onupdate="CASCADE", ondelete="CASCADE").create()
    ForeignKeyConstraint([stock.c.r_id], [rate.c.id], onupdate="CASCADE", ondelete="CASCADE").create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata = MetaData(bind=migrate_engine)
    item = Table("items", metadata, autoload=True)
    rate = Table("rate", metadata, autoload=True)
    stock = Table("stock", metadata, autoload=True)
    ForeignKeyConstraint([rate.c.item_code], [item.c.code], onupdate="CASCADE", ondelete="CASCADE").drop()
    ForeignKeyConstraint([stock.c.item_code], [item.c.code], onupdate="CASCADE", ondelete="CASCADE").drop()
    ForeignKeyConstraint([stock.c.r_id], [rate.c.id], onupdate="CASCADE", ondelete="CASCADE").drop()

