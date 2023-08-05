f = open("sample.txt","r")  #opens a file in a
#if we dont mention anything then by default it will open in read mode..
b = f.read() #function used to read data 
print(b)  #to read it is necessary to have a file of that name
f.close()

#if we write something in bracket of read then it will store that no of characters only.
 #b=f.read(5)  #read only 5 char


#other methods of read..
a=open("sample.txt","r")
c=a.readline() #reads only first line
print(c) #can be use multi times unlike read to print all lines with one new line
a.close

# r for read
# w for write
# a for append
# + for update (Read+write)
# rb for binary file
# rt for text file but by default it is written 