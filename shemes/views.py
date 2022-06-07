from sqlalchemy import insert
from sqlalchemy import select
from settings.settings import conn
from shemes.models import customers, items, orders, order_lines

# 1-ый Способ создания данных в БД
# ins = customers.insert().values(
#     first_name='Dmitriy',
#     last_name='Yatsenko',
#     username='Moseend',
#     email='moseend@mail.com',
#     address='Shemilovskiy 2-Y Per., bld. 8/10, appt. 23',
#     town=' Vladivostok'
# )
# r = conn.execute(ins)  <- та самая место где создает данные в БД


# 2-ой Способ создания данных в БД
# ins = insert(customers).values(
#     first_name='Valeriy',
#     last_name='Golyshkin',
#     username='Fortioneaks',
#     email='fortioneaks@gmail.com',
#     address='Narovchatova, bld. 8, appt. 37',
#     town='Magadan'
# )
#
# r = conn.execute(ins)
# print(r.inserted_primary_key)  # Вывод в терминал(консоль) id созданного записи

# 3-ой Способ и самый наилучший способ создания записи в БД
# ins = insert(customers)
#
# r = conn.execute(ins,
#      first_name="Vadim",
#      last_name="Moiseenko",
#      username="Antence73",
#      email="antence73@mail.com",
#      address='Partizanskiy Prospekt, bld. 28/А, appt. 51',
#      town=' Vladivostok'
# )


# 4-ый Способ но создается сразу несколько объектов в БД
# data = [
#     {
#         "first_name": "Vladimir",
#         "last_name": "Belousov",
#         "username": "Andescols",
#         "email": "andescols@mail.com",
#         "address": "Ul. Usmanova, bld. 70, appt. 223",
#         "town": " Naberezhnye Chelny"
#     },
#     {
#         "first_name": "Tatyana",
#         "last_name": "Khakimova",
#         "username": "Caltin1962",
#         "email": "caltin1962@mail.com",
#         "address": "Rossiyskaya, bld. 153, appt. 509",
#         "town": "Ufa"
#     },
#     {
#         "first_name": "Pavel",
#         "last_name": "Arnautov",
#         "username": "Lablen",
#         "email": "lablen@mail.com",
#         "address": "Krasnoyarskaya Ul., bld. 35, appt. 57",
#         "town": "Irkutsk"
#     },
# ]
#
# ins = insert(customers)  # Создание объекта для вставки данных в БД. То есть объект создается но еще не сохраняется в БД
# r = conn.execute(ins, data)  # Выполнение запроса на добавление данных в БД. Сохранение данных в БД
# print(r.rowcount)  # Вывод в терминал(консоль) количества добавленных записей. inserted_primary_key и rowcount отличаются по задаче

# 5-ый Способ но создается сразу несколько объектов в БД
# items_list = [
#     {
#         "name":"Chair",
#         "cost_price": 9.21,
#         "selling_price": 10.81,
#         "quantity": 6
#     },
#     {
#         "name":"Pen",
#         "cost_price": 3.45,
#         "selling_price": 4.51,
#         "quantity": 3
#     },
#     {
#         "name":"Headphone",
#         "cost_price": 15.52,
#         "selling_price": 16.81,
#         "quantity": 50
#     },
#     {
#         "name":"Travel Bag",
#         "cost_price": 20.1,
#         "selling_price": 24.21,
#         "quantity": 50
#     },
#     {
#         "name":"Keyboard",
#         "cost_price": 20.12,
#         "selling_price": 22.11,
#         "quantity": 50
#     },
#     {
#         "name":"Monitor",
#         "cost_price": 200.14,
#         "selling_price": 212.89,
#         "quantity": 50
#     },
#     {
#         "name":"Watch",
#         "cost_price": 100.58,
#         "selling_price": 104.41,
#         "quantity": 50
#     },
#     {
#         "name":"Water Bottle",
#         "cost_price": 20.89,
#         "selling_price": 25.00,
#         "quantity": 50
#     },
# ]
#
# order_list = [
#     {
#         "customer_id": 1
#     },
#     {
#         "customer_id": 1
#     }
# ]
#
# order_line_list = [
#     {
#         "order_id": 1,
#         "item_id": 1,
#         "quantity": 5
#     },
#     {
#         "order_id": 1,
#         "item_id": 2,
#         "quantity": 2
#     },
#     {
#         "order_id": 1,
#         "item_id": 3,
#         "quantity": 1
#     },
#     {
#         "order_id": 2,
#         "item_id": 1,
#         "quantity": 5
#     },
#     {
#         "order_id": 2,
#         "item_id": 2,
#         "quantity": 5
#     },
# ]
#
# r = conn.execute(insert(items), items_list)  #  Выполнение запроса на добавление данных в БД. Сохранение данных в БД
# print(r.rowcount)  # Выводит
# r = conn.execute(insert(orders), order_list)
# print(r.rowcount)
# r = conn.execute(insert(order_lines), order_line_list)
# print(r.rowcount)


# s = select([customers])  # тут мы объявляем запрос на выборку данных из БД
# r = conn.execute(s)  # Выполнение запроса на выборку данных из БД. Вывод данных из БД
# print(r.fetchall())  # метод fetchall() возвращает все записи из БД

# rs = conn.execute(s)  # Выполнение запроса на выборку данных из БД. Вывод данных из БД
# for row in rs:  # перебор всех записей из набора данных из rs
#     print(row)

# print(r.fetchone())  # Извлекает следующую запись из результата. Если других записей нет, то последующие вызовы вернут None
# print(r.fetchone())  # верхний вызов вернет customers(1,  'Dmitriy', ....) а второй вызов вернет customers(2,  'Valeriy', ....)

# print(r.fetchmany(3))  # метод fetchmany(2) возвращает две записи из БД, если не передать параметр, то возвращает первую запись, если передать параметр 3, то возвращает три записи

# print(r.first())  # метод first() возвращает первую запись из БД
#
# print(r.rowcount)  # Выводит количество записей в БД
#
# print(r.keys())  # Выводит ключи всех записей из БД

# print(r.scalar())  # Возвращает первую колонку первой записи и закрывает соединение. Если результата нет, то возвращает None


# row = r.fetchone()
# print(row)
# print(type(row))
# print(row['id'], row['first_name'])  # доступ к данным по названию колонки
# print(row[0], row[1])  # доступ к данным по индексу
# print(row[customers.c.id], row[customers.c.first_name])  # доступ к данным через объект класса
# print(row.id, row.first_name)  # доступ к данным, как к атрибуту


########################
# Пример запроса на выборку данных из БД, условии для фильрации

# Запрос вернет все элементы, цена которых выше 20.
# s = select([items]).where(items.c.cost_price > 20)  # тут мы фильтруем items по полю cost_price и выбираем только те записи, где значение поля cost_price больше 20
# print(s)  # выводим запрос на выборку данных из БД
# r = conn.execute(s)  # Выполнение запроса на выборку данных из БД. Вывод данных из БД
# print(r.fetchall())  # вернем все отфильтрованные записи


# Дополнительные условия можно задать, просто добавив несколько вызовов метода where()
s = select([items]).where(items.c.cost_price + items.c.selling_price > 50).where(items.c.quantity > 10)
r = conn.execute(s)
print(s)
print(r.fetcall())
