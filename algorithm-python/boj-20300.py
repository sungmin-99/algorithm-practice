n = int(input())
arr = list(map(int,input().split()))
arr.sort()
if n % 2 == 0:
    ans = 0
else:
    ans = arr[-1]
    arr.remove(arr[-1])
for i in range(n//2+1):
    if ans < arr[i]+arr[len(arr)-1-i]:
        ans = arr[i]+arr[len(arr)-1-i]
print(ans)