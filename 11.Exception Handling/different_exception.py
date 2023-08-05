while(True):
    try:
        a=int(input("Enter a num :\n"))
        c=1/a
        print(c)

    except ValueError as e:
        print("Enter a valid no\n")

    except ZeroDivisionError as e:
        print("make sure u havent enter 0\n")

    except:
        print("invalid")