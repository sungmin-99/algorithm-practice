n, c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
start = 1
stop = arr[-1] - arr[0]
ans = 0

while start <= stop:
    mid = (start + stop) // 2
    last = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= last + mid:
            cnt += 1
            last = arr[i]
    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        stop = mid - 1
print(ans)