n, k = map(int,input().split())
arr = list(map(int,input().split()))
cha = []
ans = 0
for i in range(n-1):
    cha.append(arr[i+1] - arr[i])
cha.sort()
for i in range(n-k):
    ans += cha[i]
print(ans)