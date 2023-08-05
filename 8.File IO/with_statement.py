with open("sample.txt","r") as f: #with fun read,write and close automatically 
    a=f.read()
    print(a)

with open("sample.txt","w") as f:
    b=f.write("uyguyghysj") #it will overwrite means replace old text with that
    print(b)

####imp if you want to wipe out whole txt just open it and do f.write(" ") it will overwrite it.