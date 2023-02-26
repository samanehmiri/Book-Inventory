#Royal Bookshop System

import getpass #prompts the user for a password without echoing
import DATABASE
import Menu
import Book

#Comment the two lines bellow if you createed the book_inventory database directly
DATABASE.DB_create()
DATABASE.Tbl_create()

while True:
    Book.clrscreen()
    print("\t.......Royal Bookshop System.......\n")
    print('royalbookshop.com/login\n')

    try:
        user_name = input("Enter your username: ")
        password = getpass.getpass('Enter your password: ')
        if user_name == 'admin' and password == 'admin':
            Menu.BookMenu()
            break
        else:
            raise ValueError
    except ValueError:
        choice = input('Invalid username or password, continue? Y/n ')
        if choice == 'Y' or choice == 'y':
            continue
        else:
            break