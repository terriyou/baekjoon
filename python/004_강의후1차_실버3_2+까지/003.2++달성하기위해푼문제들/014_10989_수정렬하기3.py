import sys

input = sys.stdin.readline

n = int(input())

cnt_list=[0 for i in range(10000)]

for cnt in range(n):
    cnt_list[int(input())-1]+=1
    
for cnt in range(0,10000):
    if cnt_list[cnt]!=0:
        for number in range(cnt_list[cnt]):
            print(cnt+1)