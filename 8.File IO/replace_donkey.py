with open("donkey.txt","r") as f:
    a=f.read()

a=a.replace("donkey","hgfjeg")

with open("donkey.txt","w") as f:
    f.write(a)

#it can be also replace for list just makw words named list and for word in words: and 
#in place of donkey write word.. you are good to go..
# if you write a.lower() then it will be converted in lower case another function