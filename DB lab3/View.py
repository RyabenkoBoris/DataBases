def tables_print(tables):
    for i in range(len(tables)):
        print(f"{i+1}.", tables[i])
    return tables[int(input("Write number of which table you want to change: "))-1]


def table_print(rows):
    number = 1
    for line in rows:
        string = f"{number}.\t"
        for elem in range(len(line)):
            string += str(line[elem]) + "\t"
        print(string)
        number += 1
    return number


def menu():
    print("""What do you want to do?
    1. Insert data in the database
    2. Remove data from database
    3. Edit data in the database
    4. Generate random data in the database
    5. Search data in the database""")
    n = int(input())
    if 1 <= n <= 5:
        return n
    else:
        print("Wrong parameter")


def find_data_menu():
    print("""Choose what to search:
    1. Search books which amount more than N
    2. Search authors with name N
    3. Search genres with name N""")
