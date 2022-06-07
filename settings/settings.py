import sqlalchemy as db

from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql+psycopg2://postgres:root@localhost/SQLAlchemy", echo=True)
engine.connect()
print(engine)
