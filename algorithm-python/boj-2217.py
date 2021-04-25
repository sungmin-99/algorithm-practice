import sys
input = sys.stdin.readline
t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))
arr.sort(key = lambda x:-x)
for i in range(t):
    arr[i] = arr[i] * (i + 1)
print(max(arr))