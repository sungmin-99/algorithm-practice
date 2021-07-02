n, k = map(int, input().split())
Min = k * (k + 1) // 2
if Min > n:
    print("-1")
elif (n - Min) % k == 0:
    print(k - 1)
else:
    print(k)