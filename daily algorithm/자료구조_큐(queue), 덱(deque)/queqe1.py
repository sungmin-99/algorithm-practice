from collections import deque

n, k = map(int, input().split())
arr = deque()
ans = []
for i in range(1, n + 1):
    arr.append(i)
while arr:
    for _ in range(k - 1):
        a = arr.popleft()
        arr.append(a)
    ans.append(arr.popleft())

print("<", end="")
for i in range(n - 1):
    print(ans[i], end=", ")
print(f"{ans[-1]}>")