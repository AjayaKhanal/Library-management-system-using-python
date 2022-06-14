import Book
import Burrow
import dateAndTime


def returnBook():
    # Burrow.status
    # while Burrow.status:
    f_name = input("Enter student's first name: ")
    l_name = input("Enter student's last name: ")
    s = "Burrower" + f_name + l_name + ".txt"
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
        returnBook()

    r = "Return" + f_name + l_name + ".txt"
    with open(r, "w+") as f:
        f.write("-------------Library Management System---------------\n")
        f.write("Date: " + dateAndTime.date() + "\tTime:" + dateAndTime.time()+"\n")
        f.write("Student Name: " + f_name + " " + l_name + "\n")
        f.write("Note: Book must be burrowed within 15 days\n")
        f.write("S.N. \t Book Name \t Price\n")
    total = 0.0
    for i in range(len(Book.bookName)):
        if Book.bookName[i] in data:
            with open(r, "a") as f:
                f.write(str(i + 1) + "\t" + Book.bookName[i] + "\t$" + Book.price[i] + "\n")
                Book.quantity[i] = int(Book.quantity[i]) + 1
            total += float(Book.price[i])
    print("\t\t\t\t" + "Price: $" + str(total))
    print("Is the book return date expired?")
    print("write YES for Yes and NO for No")
    verify = input(":")
    if verify.upper() == "YES":
        day = int(input("No. of days late: "))
        fine = 1 * day
        with open(r, "a")as f:
            f.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
        total = total + fine
        print("Fine: " + str(fine))
    elif verify.upper() == "NO":
        return
    else:
        print("Please write correctly")
        returnBook()
    print("Total: $", str(total))
    with open(r, "a")as f:
        f.write("\t\t\t\t\tTotal: $" + str(total))
    with open(r, "r")as f:
        content = f.readlines()
        for x in content:
            print(x)

    with open("bookDetails.txt", "w+") as f:
        for i in range(len(Book.bookName)):
            f.write(Book.bookName[i] + "," + Book.author[i] + "," + str(Book.quantity[i]) + "," + "$" +
                    Book.price[i] + "\n")
