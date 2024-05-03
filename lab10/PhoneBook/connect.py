import psycopg2


conn = psycopg2.connect(
    dbname="suppliers",
    user="postgres",
    password="170206",
    host="localhost"
)

cursor = conn.cursor()

def hello():
    print("What you want?(1 - Insert, 2 - Update, 3 - Delete, 4 - Query):")
    way = input()
    if way == "1":
        return "C"
    elif way == "2":
        return "U"
    elif way == "3":
        return "D"
    elif way == "4":
        return "Q"


def insert():
    Full_Name = input("Enter your name: ")
    Phone_Number = input("Enter your phone number: ")

    cursor.execute(
        "INSERT INTO phonebook (Full_Name, Phone_Number) VALUES (%s, %s)",
        (Full_Name, Phone_Number)
    )


def delete():
    print("What's Name do u want to delete?")
    user = input()
    sql = f'''DELETE FROM phonebook WHERE Full_Name = '{user}';'''
    cursor.execute(sql)

def update():
    print("What do u want update? (1 - Name, 2 - phone)")
    if input() == "1":
        print("What's old name")
        old_user = input()
        print("What's new name?")
        new_user = input()
        sql = f'''UPDATE phonebook SET Full_Name = '{new_user}' WHERE Full_Name = '{old_user}'; '''
    elif input() == "2":
        print("What's old phone")
        old_phone = input()
        print("What's new phone?")
        new_phone = input()
        sql = f'''UPDATE phonebook SET Phone_Number = '{new_phone}' WHERE Phone_Number = '{old_phone}'; '''
    cursor.execute(sql)

def query():
    print("What's column do u want? (1 - Name, 2 - phone, 3 - all)")
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
            sql = f'''SELECT * phonebook WHERE Full_Name LIKE '{condition}';'''
        elif select == "2":
            sql = f'''SELECT * phonebook WHERE Phone_Number LIKE '{condition}';'''
        else:
            sql = f'''SELECT * FROM phonebook WHERE {condition};'''
    else:
        if select == "1":
            sql = f'''SELECT Full_Name FROM phonebook;'''
        elif select == "2":
            sql = f'''SELECT Phone_Number FROM phonebook;'''
        else:
            sql = f'''SELECT * FROM phonebook;'''
    cursor.execute(sql)
    answer = cursor.fetchall()
    for row in answer:
        print(row)

what = hello()

if what == "C":
    insert()
elif what == "D":
    delete()
elif what == "U":
    update()
elif what == "Q":
    query()

conn.commit()
print("Succes!")


cursor.close()
conn.close()