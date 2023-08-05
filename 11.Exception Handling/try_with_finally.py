try:
    a=int(input("Enter a no"))
    b=1/a
except Exception as e:
    print(e)
    exit()
finally:
    print("I am finally block")#this will run at any cost
    #for eg if we exit code in except block then also it will run
