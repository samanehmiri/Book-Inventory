import Book

def BookMenu():
    while True:
        Book.clrscreen()
        print("\t\t\t Welcome to Royal Bookshop System\n")
        print("*************************************")
        print("1. Add book")
        print("2. Search book")
        print("3. Delete book")
        print("4. Update Book")
        print("5. Exit")
        print("*************************************")
        choice = int(input("Enter your choice between 1 to 5: "))
        if choice == 1:
            Book.insertData()
        elif choice == 2:
            Book.searchBook()
        elif choice == 3:
            Book.deleteBook()
        elif choice == 4:
            Book.UpdateBook()
        elif choice == 5:
            break
        else:
            print('Your choice must be between 1 to 5, try again: ')