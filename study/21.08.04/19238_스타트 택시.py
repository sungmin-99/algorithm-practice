from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def emptytaxi(x, y):
    q = deque()
    visit[x][y] = 1
    q.appendleft((x, y))
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if visit[nx][ny] or graph[nx][ny] == 1:
                continue
            if passenger[nx][ny]:
                go = passenger[nx][ny]
                passenger[nx][ny] = 0
                return visit[x][y], nx, ny, go
            q.appendleft((nx, ny))
            visit[nx][ny] = visit[x][y] + 1
    return 10 ** 10, 1, 1, 1

def fulltaxi(x, y, go):
    q = deque()
    visit[x][y] = 1
    q.appendleft((x, y))
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if visit[nx][ny] or graph[nx][ny] == 1:
                continue
            if goal[nx][ny] == go:
                return visit[x][y], nx, ny
            q.appendleft((nx, ny))
            visit[nx][ny] = visit[x][y] + 1
    return 10 ** 10, 1, 1, 1

n, m, fuel = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
x, y = map(int, input().split())
passenger = [[0] * n for _ in range(n)]
goal = [[0] * n for _ in range(n)]
for i in range(1, m + 1):
    a, b, c, d = map(int, input().split())
    passenger[a - 1][b - 1] = i
    goal[c - 1][d - 1] = i

x -= 1
y -= 1
for _ in range(m):
    visit = [[0] * n for _ in range(n)]
    useFuel, x, y, go = emptytaxi(x, y)
    if useFuel <= fuel:
        fuel -= useFuel
        visit = [[0] * n for _ in range(n)]
        useFuel, x, y = fulltaxi(x, y, go)
        if useFuel <= fuel:
            fuel += useFuel
        else:
            fuel = -1
            break
    else:
        fuel = -1
        break
print(fuel)