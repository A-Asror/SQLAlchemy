# from settings import settings
#
# from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, Numeric, CheckConstraint, engine
# from datetime import datetime
#
# metadata = MetaData()
# # metadata.drop_all(engine)
#
# customers = Table('customers', metadata,
#     Column('id', Integer(), primary_key=True),
#     Column('first_name', String(100), nullable=False),
#     Column('last_name', String(100), nullable=False),
#     Column('username', String(50), nullable=False),
#     Column('email', String(200), nullable=False),
#     Column('address', String(200), nullable=False),
#     Column('town', String(50), nullable=False),
#     Column('created_on', DateTime(), default=datetime.now),
#     Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
# )
#
#
# items = Table('items', metadata,
#     Column('id', Integer(), primary_key=True),
#     Column('name', String(200), nullable=False),
#     Column('cost_price', Numeric(10, 2), nullable=False),
#     Column('selling_price', Numeric(10, 2),  nullable=False),
#     Column('quantity', Integer(), nullable=False),
#     CheckConstraint('quantity > 0', name='quantity_check')
# )
#
#
# orders = Table('orders', metadata,
#     Column('id', Integer(), primary_key=True),
#     Column('customer_id', ForeignKey('customers.id')),
#     Column('date_placed', DateTime(), default=datetime.now),
#     Column('date_shipped', DateTime())
# )
#
#
# order_lines = Table('order_lines', metadata,
#     Column('id', Integer(), primary_key=True),  # s
#     Column('order_id', ForeignKey('orders.id')),
#     Column('item_id', ForeignKey('items.id')),
#     Column('quantity', Integer())
# )
#
# metadata.create_all(settings.engine)  # создаем таблицы в БД
