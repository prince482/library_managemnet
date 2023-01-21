class Library:
    def __init__(self, bookslist, name):
        self.bookslist = bookslist
        self.name = name
        self.lenDict = {}

    def displayBook(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)

    def addBook(self, book):
        if book in bookslist:
            print("Book alrady exists")
        else:
            self.bookslist.append(book)
            bookDataBase = open("libraryDataBase.txt", 'a')
            bookDataBase.write('\n')
            # to get new line in the text file\
            bookDataBase.write(book)
            print('Book added')

    def lendBook(self, book, user):
        print("------------>>>", bookslist)
        if book in bookslist: 
            print("------------", book)
            if book not in self.lenDict.keys():
                self.lenDict.update({book:user})
                print('Book has been lended. Database updated')
            else:
                print(f"Book has already being used by {self.lenDict[book]}")
        else:
            print("Apologies! we don't have this book in our Library")

    def returnBook(self, book):
        if book in self.lenDict.keys():
            self.lenDict.pop(book)
            print('Book returned sucuessfully')
        else:
            print('The book does not exit in the book lending database.')


def main():
   #  library = Library(bookslist,'libraryDataBase')
    while(True):
        print(f"Welcome to the cooding library. Following are the options")
        choice = '''
        1. Display Books
        2. Lend a Book
        3. ADD a Book
        4. Return a Book
        '''
        print(choice)
        userinput = input("Enter Q to quit and C to continue: - ")
        #  userinput.replace(" ","")
        
    # input = userinput.upper()

        if userinput == 'c':
            userChoice = int(input("Select an option mentioned above: - "))

            if userChoice == 1:
                library.displayBook()

            elif userChoice == 2:
                book = input('Enter the name of the book you want to lend: - ')
                user = input("Enter the name of the user: - ")
                library.lendBook(book, user)

            elif userChoice == 3:
                book = input("Enter the book you want to add to the library")
                library.addBook(book)

            elif userChoice == 4:
                book = input("Enter the name of the book you want to return: ")
                library.returnBook(book)

            else:
                print("Please choose the correct option")

        elif userinput == 'Q':
            break

        else:
            print("Please enter the valid option")

if __name__ == '__main__':
    bookslist = []
    databaseName = input("Enter the name of the databasefile with extension: - ")
    bookDatabse = open(databaseName, 'r')

    for book in bookDatabse:
        bookslist.append(book)
    library = Library(bookslist,'libraryDataBase')
    main()
