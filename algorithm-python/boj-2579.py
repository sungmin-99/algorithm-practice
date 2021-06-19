n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))
dp = [0] * (n + 10)
if n < 3:
    stairs.append(0)
    stairs.append(0)
dp[1], dp[2] = stairs[1], stairs[1] + stairs[2]
dp[3] = max(stairs[2] + stairs[3], dp[1] + stairs[3])
for i in range(4,n + 1):
    dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])
print(dp[n])