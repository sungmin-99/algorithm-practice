import sys

input = sys.stdin.readline

n, k = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input()))

check = 0
for i in range(n):
    if k >= money[n - i - 1]:
        check += k // money[n - 1 - i]
        k = k % money[n - 1 - i]
print(check)