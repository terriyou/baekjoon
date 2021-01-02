
n = int(input())
cute_l = []

for i in range(n):
    cute_l.append(int(input()))

if cute_l.count(0) > cute_l.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")