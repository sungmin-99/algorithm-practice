n, w = map(int, input().split())
arr = []
coin = 0
for _ in range(n):
    arr.append(int(input()))
for i in range(n - 1):
    if arr[i] < arr[i + 1]:
        coin += w // arr[i]
        w -= (w // arr[i]) * arr[i]
    elif arr[i] > arr[i + 1]:
        w += coin * arr[i]
        coin = 0
print(w + coin * arr[-1])