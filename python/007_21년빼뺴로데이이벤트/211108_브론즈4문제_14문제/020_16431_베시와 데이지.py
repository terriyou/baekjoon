b = list(map(int, input().split()))
d = list(map(int, input().split()))
j = list(map(int, input().split()))

b_t_j_x = b[0] - j[0]
b_t_j_y = b[1] - j[1]

b_t_j = [abs(b[0] - j[0]), abs(b[1] - j[1])]
d_t_j = abs(d[0] - j[0]) + abs(d[1] - j[1])
b_t_j = sum(b_t_j) - min(b_t_j)
if b_t_j > d_t_j:
    print("daisy")
elif b_t_j < d_t_j:
    print("bessie")
else:
    print("tie")