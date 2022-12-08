import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Tables import Author, Series, Book, Genre, BookGenre
import time


class Model:
    def __init__(self, dbname, user_name, password, host):
        try:
            self.__context = psycopg2.connect(host=host, user=user_name, password=password, database=dbname)
            self.__cursor = self.__context.cursor()
            self.__table_names = None
            self.engine = create_engine('postgresql://postgres:qwerty@localhost:5432/book_shop', echo=True)
            self.Session = sessionmaker(bind=self.engine)
            self.s = self.Session()
        except Exception as _ex:
            print("[INFO] Error while working with PostgresSQL", _ex)

    def __del__(self):
        if self.__context:
            self.__cursor.close()
            self.__context.close()

    def get_table_names(self):
        if self.__table_names is None:
            self.__cursor.execute("""SELECT table_name 
                             FROM information_schema.tables
                             WHERE table_schema = 'public'""")
            self.__table_names = [table[0] for table in self.__cursor]
        return self.__table_names

    def get_column_types(self, table_name):
        self.__cursor.execute("""SELECT column_name, data_type 
            FROM information_schema.columns
           WHERE table_schema = 'public' AND table_name = %s
           ORDER BY table_schema, table_name""", (table_name,))
        return self.__cursor.fetchall()

    def get_column_names(self, table_name):
        self.__cursor.execute("""
            SELECT column_name FROM information_schema.columns
            WHERE table_schema = 'public' AND table_name = %s
            ORDER BY table_schema, table_name""", (table_name,))
        return [x[0] for x in self.__cursor.fetchall()]

    def get_table_data(self, table_name):
        id_column = self.get_column_types(table_name)[0][0]
        cursor = self.__cursor
        try:
            cursor.execute(
                sql.SQL('SELECT * FROM {} ORDER BY {} ASC').format(sql.Identifier(table_name), sql.SQL(id_column)))
        except Exception as e:
            return str(e)
        return [col.name for col in cursor.description], cursor.fetchall()

    def get_foreign_key_info(self, table_name):
        self.__cursor.execute(""" 
           SELECT kcu.column_name, ccu.table_name AS 
           foreign_table_name, ccu.column_name AS foreign_column_name 
           FROM information_schema.table_constraints AS tc 
              JOIN information_schema.key_column_usage AS kcu
                 ON tc.constraint_name = kcu.constraint_name
                 AND tc.table_schema = kcu.table_schema
                JOIN information_schema.constraint_column_usage AS ccu
                 ON ccu.constraint_name = tc.constraint_name
                 AND ccu.table_schema = tc.table_schema
           WHERE tc.constraint_type = 'FOREIGN KEY' AND 
                          tc.table_name=%s;""", (table_name,))
        return self.__cursor.fetchall()

    def insert_data(self, table_name, values):
        if table_name == 'author':
            data = Author(name=values[0])
        elif table_name == 'series':
            data = Series(name=values[0], book_numbers=values[1], author_id=values[2])
        elif table_name == 'book':
            data = Book(name=values[0], price=values[1], amount=values[2],
                        publication_date=values[3], series_id=values[4])
        elif table_name == 'genre':
            data = Genre(name=values[0])
        elif table_name == 'book_genre':
            data = BookGenre(book_id=values[0], genre_id=values[1])
        self.s.add(data)
        self.s.commit()
        self.s.close()

    def delete_data(self, table_name, cond):
        if table_name == 'author':
            data = self.s.query(Author).get(cond)
        elif table_name == 'series':
            data = self.s.query(Series).get(cond)
        elif table_name == 'book':
            data = self.s.query(Book).get(cond)
        elif table_name == 'genre':
            data = self.s.query(Genre).get(cond)
        elif table_name == 'book_genre':
            data = self.s.query(BookGenre).get(cond)
        self.s.delete(data)
        self.s.commit()
        self.s.close()

    def change_data(self, table_name, values, cond):
        if table_name == 'author':
            data = self.s.query(Author).get(cond)
            data.name = values[0]
        elif table_name == 'series':
            data = self.s.query(Series).get(cond)
            data.name = values[0]
        elif table_name == 'book':
            data = self.s.query(Book).get(cond)
            data.name = values[0]
            data.price = values[1]
            data.amount = values[2]
            data.publication_date = values[3]
            data.series_id = values[4]
        elif table_name == 'genre':
            data = self.s.query(Genre).get(cond)
            data.name = values[0]
        self.s.commit()
        self.s.close()

    def generate_data(self, table_name, count):
        types = self.get_column_types(table_name)
        fk_array = self.get_foreign_key_info(table_name)
        select_subquery = ""
        insert_query = "INSERT INTO " + table_name + " ("
        for i in range(1 if "id" in self.get_table_data(table_name)[0] else 0, len(types)):
            t = types[i]
            name = t[0]
            kind = t[1]
            fk = [x for x in fk_array if x[0] == name]
            if fk:
                select_subquery += ('(SELECT {} FROM {} ORDER BY RANDOM(), ser LIMIT 1)'.format(fk[0][2], fk[0][1]))
            elif kind == 'integer':
                select_subquery += 'trunc(random()*100)::INT'
            elif kind == 'character varying':
                select_subquery += 'chr(trunc(65 + random()*25)::INT) || chr(trunc(65 + random() * 25)::INT)'
            elif kind == 'date':
                select_subquery += """ date(timestamp '2014-01-10' + random() * 
                (timestamp '2020-01-20' - timestamp '2014-01-10'))"""
            else:
                continue
            insert_query += name
            if i != len(types) - 1:
                select_subquery += ','
                insert_query += ','
            else:
                insert_query += ') '

        self.__cursor.execute(
            insert_query + "SELECT " + select_subquery + "FROM generate_series(1," + str(count) + ") as ser")
        self.__context.commit()

    def find_data(self, num):
        if num == 1:
            string = f"SELECT * FROM book WHERE amount > {int(input('Write min. amount: '))}"
            t1 = time.perf_counter()
            self.__cursor.execute(string)
            return self.__cursor.fetchall(), t1
        elif num == 2:
            string = f"SELECT * FROM author WHERE name = '{input('Write name: ')}'"
            t1 = time.perf_counter()
            self.__cursor.execute(string)
            return self.__cursor.fetchall(), t1
        elif num == 3:
            string = f"SELECT * FROM genre WHERE name = '{input('Write name: ')}'"
            t1 = time.perf_counter()
            self.__cursor.execute(string)
            return self.__cursor.fetchall(), t1
