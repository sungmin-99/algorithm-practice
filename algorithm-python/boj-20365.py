n = int(input())
rnb = input()
check = 1
for i in range(1, n):
    if rnb[i] != rnb[i - 1]:
        check += 1
print(check // 2 + 1)