def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

n, m = map(int, input().split())
dp = [False] + [False] + [True] * (m + 1)
for i in range(2, int(m ** 0.5) + 1):
    if prime(i) == True:
        for k in range(i * 2,m + 1, i):
            dp[k] = False
for i in range(n,m+1):
    if dp[i] == True:
        print(i)