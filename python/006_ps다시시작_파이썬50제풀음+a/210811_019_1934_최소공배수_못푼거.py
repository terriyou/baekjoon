n = int(input())
cm = []

from functools import reduce

def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
                return 0
        ans *= n
    return ans


for _ in range(n):
    nums = list(map(int, input().split()))
        
    if nums[0] % nums[1] == 0:
        print(nums[0])
    elif nums[1] % nums[0] == 0:
        print(nums[1])
    else:
        if nums[0] > nums[1]:
            for j in range(1,nums[0]+1):
                if nums[0] % j == 0 or nums[1] % j == 0 and j not in cm and j != multiply(cm):
                    cm.append(j)
                    print(j)
        if nums[1] > nums[0]:
            for k in range(1,nums[1]+1):
                if nums[1] % k == 0 or nums[0] % k == 0 and k not in cm and k != multiply(cm):
                    cm.append(k)
                    print(k)
        
        print(multiply(cm))

    cm = []

    