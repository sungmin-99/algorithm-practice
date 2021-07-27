#시간초과
from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != 1 and (graph[nx][ny] > graph[x][y] or graph[nx][ny] == 0):
                graph[nx][ny] = graph[x][y] + 1
                q.appendleft((nx, ny))
    return

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
graphCopy = copy.deepcopy(graph)

virus = []
q = deque()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))
virusCom = combinations(virus, m)

ans = 10 ** 10
for i in virusCom:
    time = 0
    graph = copy.deepcopy(graphCopy)
    for j in i:
        q.append(j)
    bfs()
    check = True
    for x in range(n):
        for y in range(n):
            time = max(time, graph[x][y])
            if graph[x][y] == 0:
                check = False
    if check == False:
        time = 10 ** 10
    ans = min(ans, time)
if ans == 10 ** 10:
    print("-1")
else:
    print(ans - 2)