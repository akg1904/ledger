from datetime import datetime

import pytz
from sqlalchemy import MetaData, Table, Column, DateTime
from migrate import *

tz = pytz.timezone('Asia/Kolkata')


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata = MetaData(bind=migrate_engine)
    user = Table("user_details", metadata, autoload=True)
    update_time = Column('update_time', DateTime(timezone=True), nullable=False, default=datetime.now(tz))
    update_time.create(user)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata = MetaData(bind=migrate_engine)
    user = Table("user_details", metadata, autoload=True)
    user.c.update_time.drop()
