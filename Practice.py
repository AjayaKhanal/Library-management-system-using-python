import datetime


class Library:
    '''
    global bookName
    global author
    global quantity
    global price
    '''

    def __init__(self):
        self.bookName = []
        self.author = []
        self.quantity = []
        self.price = []
        self.first()

    def first(self):
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
            # self.book()
            self.burrow()
        elif a.upper() == "R":
            self.book()
            self.returnBook()
        elif a.upper() == "E":
            print("Thank you for using library management system")
            return
        else:
            print("Please input as suggested.")
        self.first()

    def book(self):
        with open("bookDetails.txt", "r") as f:
            content = f.readlines()
            for x in content:
                content = x.strip("\n")
            for i in range(len(content)):
                index = 0
                for b in content[i].split(','):
                    if (index == 0):
                        self.bookName.append(b)
                    elif (index == 1):
                        self.author.append(b)
                    elif (index == 2):
                        self.quantity.append(b)
                    elif (index == 3):
                        self.price.append(b.strip("$"))
                    index += 1

    def date(self):
        current = datetime.datetime.now()
        return str(current.date())

    def time(self):
        current = datetime.datetime.now()
        return str(current.time())

    def burrow(self):
        self.book()
        book_name = self.bookName
        lend = False
        while True:
            name = input("Enter your full name: ")
            if name.isalpha():
                break
            print("Please fill alphabet letters")

        s = "Burrower" + name + ".txt"
        with open(s, "w+") as f:
            f.write("-------------Library Management System---------------\n")
            f.write("--------------Book Burrowing details-----------------\n")
            f.write("Date: " + self.date() + "\tTime:" + self.time()+"\n")
            f.write("Student Name: " + name+"\n")
            f.write("S.N. \t book name \t author \n")

        while lend == False:
            print("Please select an option below: ")
            for i in range(len(book_name)):
                print("Enter", i, "to borrow book ", book_name[i])

            try:
                choose = int(input("Enter your choice: "))
                try:
                    if int(self.quantity[choose]) > 0:
                        print("Book is available for burrowing")
                        with open(s, "a") as f:
                            f.write("1 \t" + self.bookName[choose] + "\t" + self.author[choose])

                        self.quantity[choose] = int(self.quantity[choose]) - 1
                        with open(s, "bookDetails.txt", "w+") as f:
                            for i in range(3):
                                f.write(self.bookName[i] + "," + self.author[i] + "," + str(self.quantity[i]) + "," + "$" + self.price[
                                    i] + "\n")

                        # for multiple book
                        loop = True
                        count = 1
                        while loop == True:
                            print("Write yes for burrowing more books and no for not")
                            next = input("Do you want to burrow more books? ")
                            if next.upper() == "YES":
                                count = count + 1
                                print("please choose another book: ")
                                for i in range(len(self.bookName)):
                                    print("Enter", i, "to borrow book", self.bookName[i])
                                choose = int(input("Enter your choice: "))
                                if int(self.quantity[choose]) > 0:
                                    print("Book is available for burrow")
                                    with open(s, "a") as f:
                                        f.write(
                                            str(count) + ". \t\t" + self.bookName[choose] + "\t\t  " + self.author[choose] + "\n")

                                    self.quantity[choose] = int(self.quantity[choose]) - 1
                                    with open("bookDetails.txt", "w+") as f:
                                        for i in range(3):
                                            f.write(self.bookName[i] + "," + self.author[i] + "," + str(
                                                self.quantity[i]) + "," + "$" + self.price[i] + "\n")
                                            lend = False
                                else:
                                    lend = False
                                    break
                            elif next.upper() == "NO":
                                print("Thank you for borrowing books ")
                                print("")
                                loop = False
                                lend = True
                            else:
                                print("Please choose correctly")
                        with open(s, "w+") as f:
                            lines = f.readlines()
                            print(lines)

                    else:
                        print("Book is not available")
                        self.burrow()
                        lend = False

                except IndexError:
                    print("Please choose book according as instructed")
            except ValueError:
                print("Please choose correctly")

    def returnBook(self):
        name = input("Enter student name: ")
        s = "Burrower: " + name + ".txt"
        try:
            with open(s, "r") as f:
                content = f.readlines()
                for i in content:
                    content = s.strip("$")
            with open(s, "r") as f:
                data = f.read()
                print(data)
        except:
            print("Incorrect name")
            self.returnBook()

        r = "Return: " + name + ".txt"
        with open(r, "w+") as f:
            f.write("-------------Library Management System---------------\n")
            f.write("Date: " + self.date() + "\tTime:" + self.time()+ "\n")
            f.write("Student Name: ", name+"\n")
            f.write("Note: Book must be burrowed within 15 days"+"\n")
            f.write("S.N. \t Book Name \t Price")
        total = 0.0
        for i in range(3):
            if self.bookName[i] in data:
                with open(r, "a") as f:
                    f.write(str(i + 1) + "\t\t" + self.bookname[i] + "\t\t$" + self.price[i] + "\n")
                    self.quantity[i] = int(self.quantity[i]) + 1
                total += float(self.price[i])
        print("\t\t\t\t\t\t" + "$" + str(total))
        print("Is the book return date expired?")
        print("Press Y for Yes and N for No")
        verify = input(":")
        if verify.upper() == "Y":
            day = int(input("No. of days late: "))
            fine = 1*day
            with open(r, "a")as f:
                f.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
            total = total + fine
        print("Total Price: $", str(total))
        with open(r, "a")as f:
            f.write("\t\t\t\t\tTotal: $" + str(total))

        with open("bookDetails.txt", "w+") as f:
            for i in range(3):
                f.write(self.bookname[i] + "," + self.authorname[i] + "," + str(self.quantity[i]) + "," + "$" +self.price[i] + "\n")


li = Library()
print(li)
