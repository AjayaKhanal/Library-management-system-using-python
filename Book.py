def book():
    global bookName
    global author
    global quantity
    global price
    bookName = []
    author = []
    quantity = []
    price = []
    with open("bookDetails.txt","r") as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
        for i in range(len(content)):
            index = 0
            for b in content[i].split(','):
                if index == 0:
                    bookName.append(b)
                elif index == 1:
                    author.append(b)
                elif index == 2:
                    quantity.append(b)
                elif index == 3:
                    price.append(b.strip("$"))
                index += 1
