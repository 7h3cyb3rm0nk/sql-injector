import mysql.connector
import pyfiglet
import sys
import time

print(pyfiglet.figlet_format("sql-injector"))


sql_username = input("enter the username: ")
sql_password = input("enter the password: ")
sql_host = input("specify the host: ")
sql_database = input("enter the database name: ")
sql_table = input("enter the table name: ")

creds = {'username':sql_username, 'password':sql_password, 'host':sql_host, 'database':sql_database}
print(f"using the credentials: {creds}")
time.sleep(0.5)

def prompt():
    print("what do you want to do")
    print("1.insert values into the database")
    print("2.exit")
    global choice 
    choice = int(input("Enter your choice: "))


def addvalues():
    mydb = mysql.connector.connect(**creds)
    cursor = mydb.cursor()
    value_list = []
    value_limit = int(input("Enter the limit: "))
    for i in range(value_limit):
        name = input("enter the name: ")
        rno = int(input("enter the rno: "))
        age = int(input("enter the age: "))
        temp_list = [name,rno, age]
        value_list.append(temp_list)
    
    for k in value_list:
        cursor.execute(f"insert into {sql_table} values('{k[0]}', {k[1]}, {k[2]});")
    
    mydb.commit()
    print("values are inserted")

prompt()

if choice == 1:
    print("this is going to insert values into the table specified")
    print("values inserted will be name, rno, age. feel free to edit the code to change the value params ;)")
    time.sleep(1)
    exit_prompt = input("do you want to continue y/N: ")
    if exit_prompt == "N" or exit_prompt == "n":
        sys.exit()
    addvalues()
elif choice == 2:
    sys.exit()

