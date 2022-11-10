from View import *
from Model import *
import time


def insert(model):
    table = tables_print(model.get_table_names())
    table_data = model.get_table_data(table)
    if 'id' in table_data[0]:
        table_data[0].remove('id')
    values = []
    for i in range(len(table_data[0])):
        values.append(input(f"Enter value for column {table_data[0][i]}: "))
    model.insert_data(table, values, table_data[0])


def delete(model):
    table = tables_print(model.get_table_names())
    table_data = model.get_table_data(table)
    table_print(table_data[1])
    model.delete_data(table, table_data[0][0], table_data[1][int(input('Choose number:')) - 1][0])


def change(model):
    table = tables_print(model.get_table_names())
    table_data = model.get_table_data(table)
    table_print(table_data[1])
    id_name = table_data[0][0]
    num = table_data[1][int(input('Choose number:')) - 1][0]
    if 'id' in table_data[0]:
        table_data[0].remove('id')
    values = []
    for i in range(len(table_data[0])):
        values.append(input(f"Enter value for column {table_data[0][i]}: "))
    model.change_data(table, values, table_data[0], num, id_name)


def random(model):
    table = tables_print(model.get_table_names())
    model.generate_data(table, int(input("Write how much to generate: ")))


def find(model):
    find_data_menu()
    n = int(input())
    data = model.find_data(n) if 1 <= n <= 3 else print("Wrong parameter")
    table_print(data)


class Controller:
    def __init__(self):
        self.__operate = menu()
        if self.__operate:
            self.operation()

    def operation(self):
        model = Model("book_shop", "postgres", "qwerty", "127.0.0.1")
        if self.__operate == 1:
            insert(model)
        elif self.__operate == 2:
            delete(model)
        elif self.__operate == 3:
            change(model)
        elif self.__operate == 4:
            random(model)
        elif self.__operate == 5:
            t1 = time.perf_counter()
            find(model)
            t2 = time.perf_counter()
            print(f"Time of searching: {t2-t1} milliseconds")
