# import
import datetime

# creating class
class LibraryManagementSystem:
    list = []

    def __init__(self, book_details):  # ,studentName,bookName,nameOfAuthor,quantity,price):
        self.book_details = book_details
        self.booksDict = {}
        print("---------Welcome to library------------------")
        print("Choose: \n D for display books \n A for add books \n B for burrow books \n R for return books \n")
        option = input("Choose any option: ")
        if option == "D" or option == "d":
            self.displayBooks()
            self.query()
        elif option == "A" or option == "a":
            self.addBooks()
            self.query()
        elif option == "B" or option == "b":
            self.burrowBooks()
            self.query()
        elif option == "R" or option == "r":
            self.returnBooks()
            self.query()
        else:
            print("Wrong input !! Please chose right option")
            self.query()

    def query(self):
        print("\n Choose: \n c for continue \n e for exit")
        query = input("Do you want to continue or exit: ")
        if query == "C" or query == "c":
            self.__init__("bookDetails.txt")
        elif query == "E" or query == "e":
            print("Thank you")
            return
        else:
            print("please choose right option")
            self.query()

    def displayBooks(self):
        global bookName
        global author
        global quantity
        global price
        id = 1
        with open(self.book_details, "r") as book:
            content = book.readlines()
            for x in content:
                content = x.strip("\n")
                content = x.split(",")

        for i in content:
            self.booksDict.update({id: {"bookName": i[0], "author": i[1], "quantity": i[2], "price": i[3]}})
            id = id + 1

        print("id", "\t", "name of book", "\t\t", "author", "\t", "quantity", "\t", "price")
        for key, value in self.booksDict.items():
            print(key, self.booksDict[key]["name of book"], "\t", self.booksDict[key]["author"], "\t",
                  self.booksDict[key]["quantity"], "\t", self.booksDict[key]["price"])

        '''
        self.booksDict.update({str(id):{"name of book": content[0][0],"author":content[0][1],"quantity":content[0][2],"price":content[0][3]}})# ,"author:":content[1],"quantity: ": content[2],"price: ": content[3]}})
        self.booksDict.update({str(id+1):{"name of book": content[1][0], "author": content[1][1],"quantity": content[1][2], "price": content[1][3]}})
        self.booksDict.update({str(id+2):{"name of book": content[2][0], "author": content[2][1],"quantity": content[2][2], "price": content[2][3]}})
        '''

    def burrowBooks(self):
        # "burrower name": [1],"burrow date": word.replace("\t", "")
        book_id = input("Enter id of the book: ")
        currentDate = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        if book_id in self.booksDict.keys():
            if not self.booksDict[book_id]["status"] == "available":
                print(f"This book is already issued.")
                return self.burrowBooks()
            elif self.booksDict[book_id]["status"] == "available":
                student_name = input("Enter student name: ")
                self.booksDict[book_id]["burrower name"] = student_name
                self.booksDict[book_id]["burrow date"] = currentDate
                self.booksDict[book_id]["status"] = "Not available"
                print("books burrowed successfully \n")
                studentDetails = student_name +".txt" 
                with open(studentDetails,'w+')as std:
                    std.write("LibraryManagementSystem \n")
                    std.write("Date and time: " + currentDate + "\n")
                    std.write("Burrower name: " +student_name +"\n")
                    std.write("id \t name of book \t author \t price")
                    std.write()# id,name of book, author,price
        else:
            print("book id not found")
            return self.burrowBooks()

    def returnBooks(self):
        book_id = input("Enter id of the book: ")
        if book_id in self.booksDict.keys():
            if self.booksDict[book_id]["status"] == "available":
                print("Incorrect id! Please check your id")
                return self.returnBooks()
            elif not self.booksDict[book_id]["status"] == "available":
                self.booksDict[book_id]["burrower name"] = ""
                self.booksDict[book_id]["burrow date"] = ""
                self.booksDict[book_id]["status"] = "available"
                print("Book is returned")
            else:
                print("Book id is not found.")

    def addBooks(self):
        num = input("How many books do you want to enter: ")
        for i in num:
            new_book = input("Enter name of the book: ")
            new_author = input("Enter author name of the book: ")
            new_quantity = input("Enter number of book: ")
            new_price = input("Enter price for the book: $")
            if new_book == "" or new_author == "" or new_quantity == "" or new_price == "":
                return self.addBooks()
            else:
                with open(self.book_details, "w") as book:
                    book.writelines(f"{new_book},{new_author},{new_quantity},'$'{new_price}\n")
                    # self.booksDict.update(str(int(max(self.booksDict))+1):{"name of the book": new_book,"burrower name": "","burrow date": "","status":"available"})
                    print(f"This book '{new_book}' has been added successfully")


l = LibraryManagementSystem("bookDetails.txt")
print(l)
'''
        self.studentName = studentName
        self.bookName = bookName
        self.nameOfAuthor = nameOfAuthor
        self.quantity = quantity
        self.price = price 

    def bookDetails(self):
        book_name = self.bookName
        name_of_author = self.nameOfAuthor
        Quantity = self.quantity
        Price = self.price

    def getBooks(self):
        Quantity +=1
'''
