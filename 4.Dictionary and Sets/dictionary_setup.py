Mydic = {
    "gochu":"moron",
    "kutta":"bitch",
    "bewakuf":"dumb"
}
print("from ",Mydic.keys()) #print only key values
a=input("Enter your hindi word :\n")
print("your translation of your word is ",Mydic[a]) #because a we writing as key i.e hindi word
#if we use mydic.get(a) then it will not throw an error even if we write something that is not present in dictionary