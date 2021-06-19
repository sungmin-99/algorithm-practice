def dfs(x, y):
    check = 0
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 0:
        return False
    graph[x][y] = 0

    check += 1
    check += dfs(x + 1, y)
    check += dfs(x - 1, y)
    check += dfs(x, y + 1)
    check += dfs(x, y - 1)
    return check

n = int(input())
graph1 = []
graph = [[0] * n for _ in range(n)]
for _ in range(n):
    graph1.append(input())
for i in range(n):
    for j in range(n):
        graph[i][j] = int(graph1[i][j])

ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            ans.append(dfs(i, j))
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])