n = int(input())

dp = [0] * (n + 5)
dp[0], dp[2], dp[4] = 1, 1, 2

i = 6
while i <= n:
    ans = 0
    for j in range(i // 4):
        j = j * 2
        ans = ans + dp[j] * dp[i - j - 2] * 2
    if i % 4 == 2:
        ans = ans + dp[(i - 2) // 2] * dp[(i - 2) // 2]
    dp[i] = ans % 987654321
    i += 2

print(dp[n])