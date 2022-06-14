import Book
import dateAndTime


def burrow():
    # global status
    # status = False
    lend = False
    while True:
        f_name = input("Enter your first name: ")
        if f_name.isalpha():
            break
        print("Please fill alphabet letters")
    while True:
        l_name = input("Enter your last name: ")
        if l_name.isalpha():
            break
        print("Please fill alphabet letters")

    s = "Burrower" + f_name + l_name + ".txt"
    with open(s, "w+") as f:
        f.write("-------------Library Management System---------------" + "\n")
        f.write("--------------Book Burrowing details-----------------" + "\n")
        f.write("Date: " + dateAndTime.date() + "\tTime:" + dateAndTime.time() + "\n")
        f.write("Student Name: " + f_name + " " + l_name + "\n")
        f.write("S.N. \t book name \t author\n")

    while not lend:
        print("Please select an option below: ")
        for i in range(len(Book.bookName)):
            print("Enter", i, "to borrow book ", Book.bookName[i])

        try:
            choose = int(input("Enter your choice: "))
            try:
                if int(Book.quantity[choose]) > 0:
                    print("Book is available for burrowing")
                    with open(s, "a+") as f:
                        f.write("1.\t" + Book.bookName[choose] + "\t" + Book.author[choose])

                    Book.quantity[choose] = int(Book.quantity[choose]) - 1

                    # for multiple book
                    loop = True
                    count = 1
                    while loop:
                        print("Write yes for burrowing more books and no for not")
                        next_ = input("Do you want to burrow more books? ")
                        if next_.upper() == "YES":
                            count = count + 1
                            print("please choose another book: ")
                            for i in range(len(Book.bookName)):
                                print("Enter", i, "to borrow book", Book.bookName[i])
                            choose = int(input("Enter your choice: "))
                            if int(Book.quantity[choose]) > 0:
                                print("Book is available for burrow")
                                with open(s, "a") as f:
                                    f.write(
                                        "\n" + str(count) + ".\t" + Book.bookName[choose] + "\t" + Book.author[choose])

                                Book.quantity[choose] = int(Book.quantity[choose]) - 1
                                with open("bookDetails.txt", "w+") as f:
                                    for i in range(len(Book.bookName)):
                                        f.write(Book.bookName[i] + "," + Book.author[i] + "," + str(
                                            Book.quantity[i]) + "," + "$" + Book.price[i] + "\n")
                                        lend = False
                            else:
                                lend = False
                                break
                        elif next_.upper() == "NO":
                            with open("bookDetails.txt", "w+") as f:
                                for i in range(len(Book.bookName)):
                                    f.write(
                                        Book.bookName[i] + "," + Book.author[i] + "," + str(Book.quantity[i]) + ",$" +
                                        Book.price[i] + "\n")
                            print("Thank you for borrowing books ")
                            with open(s, "r") as f:
                                content = f.readlines()
                                for x in content:
                                    print(x)
                            print()
                            loop = False
                            lend = True
                            # status = True
                        else:
                            print("Please choose correctly")
                else:
                    print("Book is not available")
                    burrow()
                    lend = False

            except IndexError:
                print("Please choose book according as instructed")
        except ValueError:
            print("Please choose correctly")
