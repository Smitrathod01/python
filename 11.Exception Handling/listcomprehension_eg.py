a=int(input("Enter your no : "))

table = [a*i for i in range(1,11)]
print(table)

with open("tables.txt","a") as f:
    f.write(str(table))
    f.write('\n')