
a = input()
for i in range(26):
    if i == 25:
        print(a.find(chr(97+i)))
    else:
        print(a.find(chr(97+i)),end=" ")

#for i in range(97,123):
#    cnt = total_str.count(chr(i))
#    print(cnt)