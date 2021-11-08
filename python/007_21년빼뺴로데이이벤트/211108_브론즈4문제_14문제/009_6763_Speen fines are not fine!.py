a = int(input())
b = int(input())

sub = b - a

if sub < 1:
    print("Congratulations, you are within the speed limit!")
elif sub < 21:
    print("You are speeding and your fine is $100.")
elif sub < 31:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")