def file(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())

    except FileNotFoundError:
        print(f"{filename} not found")


file("1.txt")
file("2.txt")
file("3.txt")

print("bye")
    