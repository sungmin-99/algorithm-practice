n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

dp = [[0 for _ in range(i + 1)] for i in range(n)]

if n == 1:
    print(tri[0][0])
else:
    dp[0][0] = tri[0][0]
    dp[1][0], dp[1][1] = tri[1][0] + tri[0][0], tri[1][1] + tri[0][0]

    for i in range(2, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + tri[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tri[i][j]

    print(max(dp[n - 1]))