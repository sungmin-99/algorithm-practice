a, b = map(int,input().split())
check = 1
while a != b:
    if b == 0:
        check = -1
        break
    if str(b)[-1] == '1':
        b = (b - 1) // 10
        check += 1
    elif b % 2 == 0:
        b = b // 2
        check += 1
    else:
        check = -1
        break
print(check)