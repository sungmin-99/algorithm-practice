n, k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
dp = [k+1] * (k+1)
dp[0] = 0
for i in range(n):
    for k in range(arr[i],k+1):
        if dp[k - arr[i]] != (k + 1):
            if dp[k] > dp[k - arr[i]] + 1:
                dp[k] = dp[k - arr[i]] + 1
if dp[k] == (k + 1):
    print("-1")
else:
    print(dp[k])