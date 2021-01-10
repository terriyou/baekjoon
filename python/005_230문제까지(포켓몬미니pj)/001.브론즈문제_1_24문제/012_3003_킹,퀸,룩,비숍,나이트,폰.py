n = list(map(int,input().split()))
piece = [1,1,2,2,2,8]
result = [str(x - y) for x, y in zip(piece, n)]
print(" ".join(result))