#BOOK MODULE
from validations import str_len_validation,date_validation,digit_validation

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

from datetime import date
import platform
import os

from tkinter import Tk
from tkinter import * 

#use tkinter to show the output of search function
window = Tk() 
window.title('Royal Bookshop System')
window.geometry("700x300")
window.withdraw() #hide master window


config = {
  'user': 'root',
  'password': '******', #paswword to connect to mysql
  'host': '127.0.0.1',
  'database': 'book_inventory'
}

#Clearing the Screen
def clrscreen():
    if platform.system() == "Darwin": #Linux: Linux, Mac: Darwin, Windows: Windows
        os.system("clear")

def close():
    window.destroy()

def insertData():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        b_id = digit_validation(input('Enter book code: '),'Book Code')
        b_name = str_len_validation(input('Enter book name: '))
        author = str_len_validation(input("Enter book's author name: "))
        price = digit_validation(input('Enter book price: '),'Price')
        pub = str_len_validation(input('Enter the publisher: '))
        qty = digit_validation(input('Enter quantity purchased: '), 'Quantity')
        date_Purchase = date_validation(input("Enter date of purchase: format(YYYY-MM-DD)"))
        query = ("INSERT INTO Book VALUES (%s,%s,%s,%s,%s,%s,%s)")
        add_record = (b_id,b_name,author,price,pub,qty, date_Purchase)
        cursor.execute(query,add_record)
        cnx.commit()
        cursor.close()
        cnx.close()
    except Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("You have entered an invalid username or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Unknown database")
        else:
            print(e)
    else:
        cnx.close()

def searchBook():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        print('How do you want to search?')
        print("1. Search by id")
        print("2. Search by date")
        print("3. Search by book name (you can enter part of name)")
        print("4. Search by book author's name")
        search_type = int(input('Enter your choice: '))
        print(f'search type {search_type}')
        if search_type == 1:
            b_id = input("Enter book id of your choice to search: ")
            query = ("SELECT * FROM Book WHERE b_id = %s")
            val = (b_id,)
            cursor.execute(query,val)
        elif search_type == 2:
            date_ = input("Enter date of purchase: format(YYYY-MM-DD)")
            date_Purchase = date.fromisoformat(date_)
            query = ("SELECT * FROM Book WHERE date_purchase = %s")
            val = (date_Purchase,)
            cursor.execute(query,val)
        elif search_type == 3:
            b_name = input("Enter book name: (you can enter part of author's name)")
            query = ("SELECT * FROM Book WHERE b_name LIKE %s")
            val = ('%'+b_name+'%',)
            cursor.execute(query,val)
        elif search_type == 4:
            author = input("Enter book authors's name: (you can enter part of author's name)")
            query = ("SELECT * FROM Book WHERE author LIKE %s")
            val = ('%'+author+'%',)
            cursor.execute(query,val)
        else:
            return
        
        i = 0
        for record in cursor:
            for j in range(len(record)):
                e = Entry(window, width=10, fg='blue')
                e.grid(row=i,column=j)
                e.insert(END, record[j])
            i+=1
        window.deiconify()
        window.mainloop()
        cnx.commit()
        cursor.close()
        cnx.close()
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
        
def deleteBook():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        b_id = input('Enter book id of your choice to delete: ')
        query = ("DELETE FROM Book WHERE b_id = %s")
        val = (b_id,)
        cursor.execute(query,val)
        cnx.commit()
        cursor.close()
        cnx.close()
        print(cursor.rowcount, 'record(s) deleted successfully.')

    except Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("You have entered an invalid username or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Unknown database")
        else:
            print(e)
    else:
        cnx.close()

def UpdateBook():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        b_id = digit_validation(input("Enter book id of your choice for update: "), 'Book Code')
        print("Fill the items:")
        b_name = str_len_validation(input('Update book name: '))
        author = str_len_validation(input("Update book's author name: "))
        price = digit_validation(input('Update book price: '), 'Price')
        pub = str_len_validation(input('Update the publisher: '))
        qty = digit_validation(input('Update quantity purchased: '), 'Quantity')
        date_Purchase = date_validation(input("Update date of purchase: format(YYYY-MM-DD)"))
        q = ("UPDATE Book SET b_name=%s, author=%s, price=%s, pub=%s, qty=%s, date_Purchase=%s WHERE b_id=%s")
        data = (b_name, author, price, pub, qty, date_Purchase, b_id)
        cursor.execute(q,data)
        cnx.commit()
        cursor.close()
        cnx.close()

    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()