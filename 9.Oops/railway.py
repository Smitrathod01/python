class Train:
 
    
    def __init__(self,name):
        self.name=name
        self.seats=30
        self.price=100

    def status(self):
        print(f"Seats available : {self.seats}")

    def status2(self) :
         print(f"Price of 1 seat : {self.price}\n")
         
a=input("Enter Train name : \n")
b=Train(a)
b.status()

for j in range(30):
    
    
    b.status2()
    print("For booking press 1 and cancellation press 0 :\n")
    c=int(input("Enter 1 or 0\n"))
    d=int(input("No of seats"))

    for i in range(d):
        if c==1:
            b.seats=b.seats-1
            print("Booked!\n")
        elif c==0 and b.seats<30:
            b.seats=b.seats+1
        else:
            print("Invalid press or cancellation is unavailabe due to all vacant seats")

    b.status()



    