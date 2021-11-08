inpt1 = [int(input()) for _ in range(4)]
inpt2 = [int(input()) for _ in range(2)]

inpt1.sort(reverse=True)
inpt2.sort(reverse=True)

print(sum(inpt1[:3]) + inpt2[0])
