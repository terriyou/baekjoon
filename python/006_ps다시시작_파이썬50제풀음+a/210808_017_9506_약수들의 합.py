inpt = int(input())
yaksu = []
flag = -1

while inpt != -1:
    for i in range(1,inpt):
        if inpt % i == 0:
            yaksu.append(i)
    if inpt == sum(yaksu):
        flag = 0
    else:
        flag = 1
    
    print(inpt,end=" ")

    if flag == 0:
        print("=",end="")
        for i in range(len(yaksu)):
            if i != len(yaksu)-1:
                print(" " + str(yaksu[i]) ,end=" +")
            else:
                print(" " + str(yaksu[i]))
    elif flag == 1:
        print("is NOT perfect.")

    flag = -1
    yaksu = []
    inpt = int(input())
