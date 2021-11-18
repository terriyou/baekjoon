flag_list = []

inpt = list(map(int, input().split()))

for i in range(1,len(inpt)):
    if inpt[i-1] - inpt[i] > 0:
        flag_list.append(0)
    elif inpt[i-1] - inpt[i] < 0:
        flag_list.append(1)
    else:
        flag_list.append(2)


if flag_list.count(1) + flag_list.count(2) == len(inpt)-1:
    print('Good')
else:
    print('Bad')