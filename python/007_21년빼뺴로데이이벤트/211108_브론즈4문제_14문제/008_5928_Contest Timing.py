inpt_d, inpt_h, inpt_m = map(int, input().split())

std_d = 11
std_h = 11
std_m = 11

inpt_total_min = inpt_d * 24 * 60 + inpt_h * 60 + inpt_m
std_min = std_d * 24 * 60 + std_h * 60 + std_m

sub = inpt_total_min - std_min

if sub < 0:
    print(-1)
else:
    print(sub)
