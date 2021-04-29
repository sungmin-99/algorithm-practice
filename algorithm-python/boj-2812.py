import sys
n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().strip()))

result = []
numK = k

for i in range(n):
    while numK > 0 and result:
        if result[len(result) - 1] < num[i]:
            result.pop()
            numK -= 1
        else:
            break
    result.append(num[i])

for i in range(n - k):
    print(result[i], end="")