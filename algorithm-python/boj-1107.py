n = input()
intN = int(n)
m = int(input())
if m == 0:
    arrFix = []
else:
    arrFix = list(map(int, input().split()))
ans = abs(100 - intN)

for i in range(1000001):
    i = str(i)
    check = False
    for k in i:
        if int(k) in arrFix:
            check = True
            break

    if check == True:
        continue
    else:
        ans = min(ans, abs(int(i) - intN) + len(i))

print(ans)