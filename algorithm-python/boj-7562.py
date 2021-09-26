from collections import deque
import sys
input = sys.stdin.readline

dx = [2, 1, -2, -1, 2, 1, -2, -1]
dy = [1, 2, -1, -2, -1, -2, 1, 2]

def bfs(x, y):
    if x == destX and y == destY:
        return 0
    q = deque()
    q.appendleft((x, y))
    visit[x][y] = 1
    while q:
        x, y = q.pop()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            if visit[nx][ny] != 0:
                continue
            if nx == destX and ny == destY:
                return visit[x][y]
            visit[nx][ny] = visit[x][y] + 1
            q.appendleft((nx, ny))

t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    destX, destY = map(int, input().split())
    visit = [[0] * n for _ in range(n)]
    print(bfs(x, y))