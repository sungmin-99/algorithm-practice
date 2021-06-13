from collections import deque

def dfs(x):
    visit[x] = True
    print(x, end=' ')
    for i in range(1, n + 1):
        if not visit[i] and graph[x][i] == 1:
            dfs(i)

def bfs(x):
    visit[x] = False
    q.appendleft(x)
    while q:
        x = q.pop()
        print(x,end=' ')
        for i in range(1, n + 1):
            if visit[i] and graph[x][i] == 1:
                q.appendleft(i)
                visit[i] = False

q = deque()
n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

dfs(v)
print()
bfs(v)