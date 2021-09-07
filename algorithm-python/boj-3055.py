from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def flood():
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] != '.':
                continue
            if water[nx][ny] == 0:
                q.appendleft((nx, ny))
                water[nx][ny] = water[x][y] + 1

def bfs():
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == 'D':
                return visit[x][y]
            if graph[nx][ny] != '.':
                continue
            if visit[nx][ny] == 0 and (visit[x][y] + 1 < water[nx][ny] or water[nx][ny] == 0):
                q.appendleft((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
    return 'KAKTUS'

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(input())

water = [[0] * m for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == '*':
            q.appendleft((i, j))
            water[i][j] = 1
flood()

visit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            q.appendleft((i, j))
            visit[i][j] = 1
print(bfs())