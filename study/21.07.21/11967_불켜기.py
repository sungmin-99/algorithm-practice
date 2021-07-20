#틀렸습니다

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def light(x, y):
    remove = []
    for i in range(len(switch)):
        if switch[i][0] == x and switch[i][1] == y:
            nx, ny = switch[i][2], switch[i][3]
            graph[nx][ny] = True
            remove.append(i)
    for i in remove[::-1]:
        del switch[i]
    return

def bfs(x, y):
    q = deque()
    q.appendleft((x, y))
    while q:
        x, y = q.pop()
        light(x, y)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 >= nx or n < nx or 0 >= ny or n < ny:
                continue
            if graph[nx][ny] == True and visit[nx][ny] == False:
                visit[nx][ny] = True
                q.appendleft((nx, ny))

n, m = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visit = [[False] * (n + 1) for _ in range(n + 1)]
graph[1][1] = True
visit[1][1] = True
switch = []

for _ in range(m):
    switch.append(list(map(int, input().split())))

bfs(1, 1)
bfs(1, 1)

cnt = 0
for i in range(n + 1):
    for j in range(n + 1):
        if graph[i][j] == True:
            cnt += 1
print(cnt)