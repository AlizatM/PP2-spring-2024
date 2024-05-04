import psycopg2
from psycopg2 import Error

pattern = ""
connection = psycopg2.connect(user="postgres",
                                  password="170206",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")

cursor = connection.cursor()

def user_command():
    print("What command you want?(1 - Insert, 2 - Update, 3 - Delete, 4 - Query, 5 - Pattern, 6 - Pagination):")
    way = input()
    if way == "1":
        return "C"
    elif way == "2":
        return "U"
    elif way == "3":
        return "D"
    elif way == "4":
        return "Q"
    elif way == "5":
        global pattern
        print("What's pattern?")
        pattern = input()
        return "P"
    elif way == "6":
        return "PA"

def find_by_pattern(pattern):
    cursor.execute("""
            SELECT * FROM phonebook 
            WHERE username LIKE %s 
            OR phone LIKE %s;
            """, (f'%{pattern}%', f'%{pattern}%'))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def insert():
    print("Введите данные:")
    username = input()
    phone = input()
    sql  = f'''CALL insert_or_update_user(%s, %s)'''
    cursor.execute(sql,(username,phone))

def query_phonebook(limit, offset):
    with connection.cursor() as cursor:
        query = """
        SELECT username, phone
        FROM PhoneBook
        ORDER BY username
        LIMIT %s
        OFFSET %s
        """
        cursor.execute(query, (limit, offset))

        rows = cursor.fetchall()
        for row in rows:
            print(row)

def delete():
    print("What you want to delete?(1- username, 2-phone)")
    whhh = input()
    if whhh == "1":
        user = input()
        sql = f'''DELETE FROM PhoneBook WHERE username = '{user}';'''
    elif whhh == "2":
        phone = input()
        sql = f'''DELETE FROM PhoneBook WHERE phone = '{phone}';'''
    cursor.execute(sql)

def update():
    print("What do u want update? (1 - username, 2 - phone)")
    if input() == "1":
        print("What's old username")
        old_user = input()
        print("What's new username?")
        new_user = input()
        sql = f'''UPDATE PhoneBook SET username = '{new_user}' WHERE username = '{old_user}'; '''
    elif input() == "2":
        print("What's old phone")
        old_phone = input()
        print("What's new phone?")
        new_phone = input()
        sql = f'''UPDATE PhoneBook SET phone = '{new_phone}' WHERE phone = '{old_phone}'; '''
    cursor.execute(sql)

def query():
    print("What's column do u want? (1 - username, 2 - phone, 3 - all)")
    select = input()
    print("Do u have filter for query? (1 - YES, 2 - NO)")
    isFilter = input()
    if isFilter == "1":
        print("What's filter?")
        condition = input()
    else:
        condition = None
    if condition:
        if select == "1":
            sql = f'''SELECT * From phonebook WHERE username LIKE '{condition}';'''
        elif select == "2":
            sql = f'''SELECT * From phonebook WHERE phone LIKE '{condition}';'''
        else:
            sql = f'''SELECT * FROM PhoneBook WHERE {condition};'''
    else:
        if select == "1":
            sql = f'''SELECT username FROM PhoneBook;'''
        elif select == "2":
            sql = f'''SELECT phone FROM PhoneBook;'''
        else:
            sql = f'''SELECT * FROM PhoneBook;'''
    cursor.execute(sql)
    answer = cursor.fetchall()
    for row in answer:
        print(row)

command = user_command()

if command == "C":
    insert()
elif command == "D":
    delete()
elif command == "U":
    update()
elif command == "Q":
    query()
elif command == "P":
    find_by_pattern(pattern)
elif command == "PA":
    print("What limit and offset?")
    lim = int(input())
    offset = int(input())
    query_phonebook(lim, offset)


connection.commit()
print("Success!")



cursor.close()
connection.close()