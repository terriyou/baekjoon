a = input()

b = input()
c = input()
total = int(a) * int(b) * int(c)
total_str = str(total)


for i in range(48,58):
    cnt = total_str.count(chr(i))
    print(cnt)