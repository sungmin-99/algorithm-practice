import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int,input().split())
    arr.append((x,y))
start = 0
check = 0
arr.sort(key = lambda x:(x[1],x[0]))
for i in arr:
    if i[0] >= start:
        start = i[1]
        check += 1
print(check)