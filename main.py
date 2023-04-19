import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher,Shop,Book, Stock, Sale

password = input("Пароль: ")

DSN = f'postgresql://postgres:{password}@localhost:5432/DZ'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

session = sessionmaker(bind=engine)
session = session()

name = input("Введите имя автора: ")
query = session.query(Stock,Book.title,Shop.name,Sale.price,Sale.date_sale)
query = query.join(Sale)
query = query.join(Shop)
query = query.join(Book)
query = query.join(Publisher)
records = query.filter(Publisher.name == (name))
for c in records:
    print(f'Название книги: {c[1]}, Магазин: {c[2]}, Стоимость: {c[3]}')
session.close()