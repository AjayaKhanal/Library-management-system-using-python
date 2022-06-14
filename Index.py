import Return
import Book
import Burrow

class Library:
    def __init__(self):
        self.first()

    def first(self):
        while True:
            print("-------------Welcome to the library!!!----------------")
            print("------------------------------------------------------")
            print("Enter D. To Display\nEnter B. To Borrow a book\nEnter R. To return a book\nEnter E. To exit")

            a = input("Select a choice: ")
            print()
            if a.upper() == "D":
                with open("bookDetails.txt", "r") as f:
                    content = f.read()
                    print(content)
                    print()

            elif a.upper() == "B":
                Book.book()
                Burrow.burrow()
            elif a.upper() == "R":
                Book.book()
                Return.returnBook()
            elif a.upper() == "E":
                print("Thank you for using library management system\n")
                return
            else:
                print("Please input as suggested.\n")


        self.first()


print(Library())


