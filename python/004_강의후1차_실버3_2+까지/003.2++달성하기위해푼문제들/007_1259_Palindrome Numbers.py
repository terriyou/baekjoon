while(1):
    inpt = input()
    rev = inpt[::-1]
    if inpt == "0":
        break
    elif inpt == rev:
        print("yes")
    else:
        print("no")