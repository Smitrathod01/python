#here if we write characters then also it will work
while(True):
   
    try:
        a=int((input("Enter a no :\n")))
        if a>=6:
            print("greater")

        else:
            print("Smaller")
  
    except Exception as e:#u can write name of exeption in place of exception
        print(f"Invalid input :{e} ")