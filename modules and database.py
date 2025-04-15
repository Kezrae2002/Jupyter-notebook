%%writefile zoo.py
def hours():
    print("Open 9-5 daily")
>> Writing zoo.py

import zoo

zoo.hours()
>>Open 9-5 daily

16.8:
from sqlalchemy import create_engine, Table, MetaData, select

engine = create_engine('sqlite:///books.db')
metadata = MetaData()
metadata.reflect(bind=engine)

books = metadata.tables['books']

query = select(books.c.title).order_by(books.c.title)

with engine.connect() as connection:
    results = connection.execute(query)
    for row in results:
        print(row.title)
