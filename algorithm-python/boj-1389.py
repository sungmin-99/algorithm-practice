from collections import deque

def bfs(x):
    person[x] = True
    q = deque()
    q.appendleft(x)

    while q:
        x = q.pop()
        for i in range(1, n + 1):
            if not person[i] and graph[x][i] == 1:
                q.appendleft(i)
                person[i] = person[x] + 1
    return sum(person) - n

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

kevin = 10**10
ans = 0
for i in range(1,n + 1):
    person = [0] * (n + 1)
    if kevin > bfs(i):
        kevin = bfs(i)
        ans = i

print(ans)