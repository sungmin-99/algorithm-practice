from collections import deque
q = deque()
ans = 1
n = int(input())
for i in range(1,n+1):
    q.append(i)
while len(q) != 1:
    q.popleft()
    ans = q.popleft()
    q.append(ans)
print(ans)