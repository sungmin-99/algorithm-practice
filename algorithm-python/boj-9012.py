n = int(input())
for i in range(n):
    stack = []
    pare = input()
    for i in range(len(pare)):
        if pare[i] == '(':
            stack.append(1)
        elif pare[i] == ')' and len(stack) != 0:
            stack.pop()
        else:
            stack.append(1)
            break
    if len(stack) != 0:
        print("NO")
    else:
        print("YES")