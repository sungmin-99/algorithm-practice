dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, d):
    # print(x, y)
    graph[x][y] = 2
    check = 0
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            dfs(nx, ny, nd)
            check = 1
            break
        d = nd
    if check == 0:
        nd = (d + 2) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if graph[nx][ny] != 1:
            dfs(nx, ny, d)
        else:
            return
    return

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dfs(r, c, d)

cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            cnt += 1
# for i in range(n):
#     print(graph[i])
print(cnt)