try:
    a=int(input("Enter a no"))
    b=1/a
except Exception as e:
    print(e)
else:
    print("I am else block")#this will run when try execute without going into the except block
