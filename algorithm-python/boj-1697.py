from collections import deque

def bfs(x):
    q = deque()
    q.appendleft(x)
    graph[x] = 1
    while q:
        x = q.pop()
        if x == k:
            return graph[x] - 1
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= max and not graph[nx]:
                graph[nx] = graph[x] + 1
                q.appendleft(nx)

n, k = map(int, input().split())
max = 10**6
graph = [0] * (max + 1)
print(bfs(n))