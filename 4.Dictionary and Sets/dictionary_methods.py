dic={
    "a":"smit",
    "b":"rathod",
    "list":[12,34,23,45],
    "c":{'d':'Eng'},
    1:2
}

print(dic.keys()) #print only keys
print(type(dic.keys()))
# print(list(dic.keys()))  #type casting 
print(dic.values()) #print only values

print(dic.items())  #with keys and values in the form of tuples

dic.update({"e":"haha"}) #use to enter key and value
print(dic.keys())  #for updating multilines form another dictionaty and put it name in update paranthesis
                   #it will also update an existing value like if we again write list in updated
                   #then previous one will remove and new value will assign

print(dic.get("b"))
print(dic["b"])
#differnce between both is that if we write some non existing key then get will return none in place of error

