inpt = []
flag = []

inpt.append(int(input()))
inpt.append(int(input()))
inpt.append(int(input()))
inpt.append(int(input()))

pos_num = 0
neg_num = 0
rei_num = 0
for i in range(3):
    flag.append(inpt[i+1] - inpt[i])
    if flag[i] <0:
        neg_num += 1
    elif flag[i] == 0:
        rei_num += 1
    else:
        pos_num += 1

if pos_num == 3:
    print("Fish Rising")
elif neg_num == 3:
    print("Fish Diving")
elif rei_num == 3:
    print("Fish At Constant Depth")
else:
    print("No Fish")