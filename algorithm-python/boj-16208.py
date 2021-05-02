n = int(input())
a = list(map(int, input().split()))

cost = 0
sum = 0
l = len(a)

for i in a:
    sum = sum + i

for i in range(0, l-1):
    sum = sum - a[i]
    cost = cost + a[i] * sum

print (cost)