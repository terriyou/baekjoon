a = input()

a_b = input()

if a_b.count('A') == a_b.count('B'):
    print("Tie")
elif a_b.count('A') > a_b.count('B'):
    print("A")
else:
    print("B")