n = int(input())

class_list = []

for i in range(n):
    class_list.append(list(input().split()))
    class_list[i].append(int(class_list[i][1]) + \
        int(class_list[i][2]) * 30 + int(class_list[i][3]) * 365 )

class_list.sort(key= lambda x :x[4])
print(class_list[-1][0])
print(class_list[0][0])