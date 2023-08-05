from pip import main


def greet(name):
    print(f"hello, {name}")

print(__name__)
if __name__ == '__main__':#it will help this program to run below lines in this program only
    a=input("Enter your name ")#this will not work in s02
    greet(a)