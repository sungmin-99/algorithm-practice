from collections import deque

def bfs():
    ans = 0
    while q:
        ans += 1
        x = q.pop()
        if x == 100:
            return visit[x] - 1
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            if graph[nx]:
                nx = graph[nx][0]
            if not(visit[nx]):
                visit[nx] = visit[x] + 1
                q.appendleft(nx)


n, m = map(int, input().split())
graph = [[] for _ in range(101)]
for i in range(n + m):
    x, y = map(int, input().split())
    graph[x].append(y)

q = deque()
q.appendleft(1)
visit = [0] * 101
visit[1] = 1
print(bfs())