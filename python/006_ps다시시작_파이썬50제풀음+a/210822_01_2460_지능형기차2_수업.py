
down = 0
up = 0
max = 0
rest = 0
for _ in range(10):
    down, up = map(int, input().split())
    rest += up - down
    if rest > max:
        max = rest
print(max)