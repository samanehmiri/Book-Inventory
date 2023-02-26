#You can create the book_inventory database directly in a mysql management tool as well

import mysql.connector


config = {
  'user': 'root',
  'password': '******', #paswword to connect to mysql
  'host': '127.0.0.1'
}

def DB_create():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS book_inventory")
    cursor.close()
    cnx.close()


def Tbl_create():
    cnx = mysql.connector.connect(**config, database='book_inventory')
    cursor = cnx.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS
                    Book(b_id int(5), b_name varchar(20),author varchar(20),
                    price int(3), bub varchar(20), qty int(3), date_Purchase Date)
                    """)
    cursor.close()
    cnx.close()