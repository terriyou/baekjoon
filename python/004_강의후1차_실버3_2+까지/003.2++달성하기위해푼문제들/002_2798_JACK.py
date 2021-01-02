import itertools

inpt = list(map(int, input().split()))
numbers = list(map(int, input().split()))

greatest = -1

for subset in itertools.combinations(numbers, 3):
    tmp = sum(list(subset))
    if tmp > greatest and inpt[1] >= tmp:
        greatest = tmp

print(greatest)
    