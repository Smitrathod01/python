class Library:
    def __init__(self,listofbook) -> None:
        self.books = listofbook

    def display(self):
        print("\nAvailable books are :")
        for book in self.books:
            print(" "+book)

    def borrow(self,bookname):
        if bookname in self.books:
            print("\nSuccesfully borrowed")
            self.books.remove(bookname)
        else:
            print("\nBook is not available")

    def returnbook(self,bookname):
        self.books.append(bookname)
        print("\nThank you for returning")
        

lib = Library(["grief","affection","harrypotter","dusktilldawn","fairytales"])
while(True):
    msg='''\nWelcome to smit's library
    press 1 : for display the available books
    press 2 : for borrow
    press 3 : for return 
    press 4 : for exit
                        '''
    print(msg)

    a = int(input("\nEnter your choice : "))

    if(a==1):
        lib.display()

    elif(a==2):
        book = input(("\nEnter book name : "))
        lib.borrow(book)

    elif(a==3):
        book = input("\nEnter book name you want to return : ")
        lib.returnbook(book)

    elif(a==4):
        break

    else:
        print("\nInvalid press")

print("Thank you using my library management system")


