from sys import stdin
from collections import Counter

_ = stdin.readline()
n_d = stdin.readline().split()
_ = int(stdin.readline())
m_d = stdin.readline().split()

c = Counter(n_d)

print(' '.join(f'{c[m_cnt]}' for m_cnt in m_d))

