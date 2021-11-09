inpt = list(map(int, input().split()))

sub_1 = inpt[1] - inpt[0]
sub_2 = inpt[2] - inpt[1]

result = sub_1 if sub_1 > sub_2 else sub_2

print(result -1)