import sys
input = sys.stdin.readline

n, m = map(int, input().split())
add = {}

for _ in range(n):
    site, ps = input().split()
    add[site] = ps

for _ in range(m):
    print(add[input().rstrip()])