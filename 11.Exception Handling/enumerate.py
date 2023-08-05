list = [23,45.45,True,"smit"]

index = 0
for item in list:
    print(index,item)
    index +=1

for index,item in enumerate(list):
    print(index,item)  #it will print item with index also