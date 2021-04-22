t = int(input())
dp = [0] * 15   #dynamic programing
dp[1],dp[2],dp[3] = 1, 2, 4

for i in range(4,len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] #점화식

for i in range(t):
    n = int(input())
    print(dp[n])