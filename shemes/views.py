# from sqlalchemy import insert, and_, or_, not_, asc, desc
# from sqlalchemy import select
# from settings.settings import conn
# from shemes.models import customers, items, orders, order_lines


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
# Пример запроса на выборку данных из БД, условии для фильрации  ORM

# Запрос вернет все элементы, цена которых выше 20.
# s = select([items]).where(items.c.cost_price > 20)  # тут мы фильтруем items по полю cost_price и выбираем только те записи, где значение поля cost_price больше 20
# print(s)  # выводим запрос на выборку данных из БД
# r = conn.execute(s)  # Выполнение запроса на выборку данных из БД. Вывод данных из БД
# print(r.fetchall())  # вернем все отфильтрованные записи


# Дополнительные условия можно задать, просто добавив несколько вызовов метода where()
# s = select([items]).where(items.c.cost_price + items.c.selling_price > 50).where(items.c.quantity > 10)
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# Вывод данных из БД изаользуя bool оператор "|" --> OR
# s = select([items]).where((items.c.cost_price > 200) | (items.c.quantity < 5))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# Вывод данных из БД изаользуя bool оператор "~" --> NOT =!
# s = select([items]).where(~(items.c.quantity == 50))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# Вывод данных из БД изаользуя bool оператор "~" --> NOT =! и оператор "&" --> AND
# s = select([items]).where(~(items.c.quantity == 50) & (items.c.cost_price < 20))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


##############################################
# Союзы в SQLAlchemy
# Условия можно объединять и с помощью функций-союзов and_(), or_() и not_(). Это предпочтительный способ добавления условий в SQLAlchemy.

#  если пред звапросом есть союз and_(items.c.quantity >= 50, items.c.cost_price < 100), то все перечисленные условия внутри союза and_()
#  переведутся на where(items.c.quantity >= 50 & items.c.cost_price < 100)  & --> AND
# s = select([items]).where(and_(items.c.quantity >= 50, items.c.cost_price < 100,))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())

#  если пред звапросом есть союз or_(items.c.quantity >= 50, items.c.cost_price < 100), то все перечисленные условия внутри союза and_()
#  переведутся на where(items.c.quantity >= 50 | items.c.cost_price < 100)  | --> OR
# s = select([items]).where(or_(items.c.quantity >= 50, items.c.cost_price < 100, ))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


#  если пред звапросом есть союз and_(items.c.quantity >= 50, items.c.cost_price < 100, not_(items.c.name == 'Headphone')), и внутри союза and_() есть союз not_()
#  то все перечисленные условия внутри союза and_() переведутся на where(items.c.quantity >= 50 & items.c.cost_price < 100 & ~(items.c.name == 'Headphone'))
# WHERE items.quantity >= :quantity_1 AND items.cost_price < :cost_price_1 AND items.name != :name_1
# s = select([items]).where(and_(items.c.quantity >= 50, items.c.cost_price < 100, not_(items.c.name == 'Headphone')))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# проверка на пустоту значения date_chipped
# WHERE orders.date_shipped IS NULL
# s = select([orders]).where(orders.c.date_shipped == None)
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# проверка на непустоту значения date_chipped
# WHERE orders.date_shipped IS NOT NULL
# s = select([orders]).where(orders.c.date_shipped != None)
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# проерка на полю first_name и есть ли first_name в перечисленном списке
# WHERE orders.first_name IN ('Valeriy', 'Vadim')
# s = select([customers]).where(customers.c.first_name.in_(["Valeriy", "Vadim"]))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())

# проерка на полю first_name и нет ли first_name в перечисленном списке, то есть зять все что не похожиж в списке
# WHERE orders.first_name NOT IN ('Valeriy', 'Vadim')
# s = select([customers]).where(customers.c.first_name.notin_(["Valeriy", "Vadim"]))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())

# between проверка в промежудке, это как в джанго __range()
# s = select([items]).where(items.c.cost_price.between(10, 20))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# not_ и between проверка на, не в промежудке
# WHERE items.cost_price NOT BETWEEN %(cost_price_1)s AND %(cost_price_2)s
# s = select([items]).where(not_(items.c.cost_price.between(10, 20)))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# Метод like() выполняет сравнение с учетом регистра.
# s = select([items]).where(items.c.name.like("Wa%"))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# Метод ilike() выполняет сравнение без учетом регистра.
# s = select([items]).where(items.c.name.ilike("wa%"))
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# Сортировка order_by(), а метод asc и desc выполняет сортировку по возрастанию и убыванию по полю.
# s = select([items]).where(items.c.quantity > 10).order_by(asc(items.c.cost_price))
# s = select([items]).where(items.c.quantity > 10).order_by(desc(items.c.cost_price))
# r = conn.execute(s)
# print(r.fetchall())


# Метод limit() принимает целое число, определяющее число записей, которые должны вернуться
# FROM items ORDER BY items.quantity LIMIT %(param_1)s
# s = select([items]).order_by(items.c.quantity).limit(2)
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# offset(n) метод овсет выбирает каждый n элемент из списка
# s = select([items]).order_by(items.c.quantity).limit(5).offset(2)
# print(s)
# r = conn.execute(s)
# print(r.fetchall())


# Ограничение колонок. Ограничить количество полей, возвращаемых запросом можно, передав название полей в виде списка в функцию select()
# s = select([items.c.name, items.c.quantity]).where(items.c.quantity == 50)
# print(s)
# r = conn.execute(s)
# print(r.keys())
# print(r.fetchall())


# Внимание items.c.selling_price * 5 — это не реальная колонка, поэтому создается анонимное имя anon_1.
# s = select([items.c.name, items.c.quantity, items.c.selling_price * 5]).where(items.c.quantity == 50)
# print(s)
# r = conn.execute(s)
# print(r.keys())  # RMKeyView(['name', 'quantity', 'anon_1'])
# print(r.fetchall())


# Колонке или выражению можно присвоить метку с помощью метода label()
# s = select([items.c.name, items.c.quantity, (items.c.selling_price * 5).label('price')]).where(items.c.quantity == 50)
# print(s)
# r = conn.execute(s)
# print(r.keys())  # RMKeyView(['name', 'quantity', 'price'])
# print(r.fetchall())

# s = select([
#     orders.c.id.label('order_id'),
#     orders.c.date_placed,
#     order_lines.c.quantity,
#     items.c.name,
#
# ]).select_from(
#     orders.join(customers).join(order_lines).join(items)
# ).where(
#     and_(
#         customers.c.first_name == "Dmitriy",
#         customers.c.last_name == "Yatsenko",
#     )
# )
#
# print(s)
# rs = conn.execute(s)
# print(rs.keys())
# print(rs.fetchall())
