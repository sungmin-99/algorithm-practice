import sys
input = sys.stdin.readline
n = int(input())
tip=[]
for _ in range(n):
    tip.append(int(input()))
tip.sort(reverse=True)
answer = 0
for i in range(n):
    if tip[i] - i >= 0:
        answer += (tip[i] - i)
print(answer)