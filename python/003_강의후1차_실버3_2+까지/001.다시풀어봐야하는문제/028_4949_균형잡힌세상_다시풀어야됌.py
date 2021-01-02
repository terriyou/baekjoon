from sys import stdin

while 1: 
    string = stdin.readline().rstrip() 
    stack = [] 
    flag = 1 
    for cha in string: 
        if cha == '(' or cha == '[': 
            stack.append(cha) 
        elif cha == ')': 
            if stack and stack[-1] == '(': 
                stack.pop() 
            else: 
                flag = 0 
                break 
        elif cha == ']': 
            if stack and stack[-1] == '[': 
                stack.pop() 
            else: 
                flag = 0 
                break 
    if string == '.': 
        break 
    print("yes" if flag and not(stack) else "no")

