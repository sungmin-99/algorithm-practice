from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def fireBfs():
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '#' and visit[nx][ny] == 0:
                q.appendleft((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
    return

def escapeBfs():
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or h <= nx or 0 > ny or w <= ny:
                return visit[x][y]
            if graph[nx][ny] != '#' and (visit[nx][ny] > visit[x][y] + 1 or visit[nx][ny] == 0):
                q.appendleft((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
    return False

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    graph = []
    visit = [[0] * w for _ in range(h)]
    for _ in range(h):
        graph.append(input())

    q = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                q.appendleft((i, j))
                visit[i][j] = 1
    fireBfs()
    # for i in range(h):
    #     print(visit[i])
    q = deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                q.appendleft((i, j))
                visit[i][j] = 1
                break
    ans = escapeBfs()
    # for i in range(h):
    #     print(visit[i])
    if ans == False:
        print('IMPOSSIBLE')
    else:
        print(ans)