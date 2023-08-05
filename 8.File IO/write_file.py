f = open("sample.txt","w") #it will create an file if it doesnt exist
f.write("I am smit rathod and i am learning python") #used to write 
f.close()

f = open("sample.txt","a") #apend used to write at last
f.write("Iam appending")
f.close() #if you dont close then it will print that many times u run it..

