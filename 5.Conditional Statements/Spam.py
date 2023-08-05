text=input("Enter your text : \n")
spam = False #use of boolean function..

if("make lot money" in text): #if this text is detect in text then returns true perfect use of in
    spam = True               #basically for text in and value == in if clause..

elif("congo" in text):
    spam = True

elif("you won a prize" in text):
    spam = True

# print(spam)  This is valid

#another way
# else:
#   spam = False #if we didnt make it on top then do this here otherwise not

if(spam):
    print("This text is spam")

else:
    print("This text is not spam")
