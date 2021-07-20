def widthUphill(x, y):
    if y - l < -1:
        return False
    for k in range(l - 1):
        if graph[x][y - k] != graph[x][y - k - 1]:
            return False
    for k in range(l):
        if visit[x][y - k] == 1:
            return False
    for k in range(l):
        visit[x][y - k] = 1
    return True

def widthDownhill(x, y):
    if y >= n - l:
        return False
    for k in range(1, l):
        if graph[x][y + k] != graph[x][y + k + 1]:
            return False
    for k in range(1, l + 1):
        if visit[x][y + k] == 1:
            return False
    for k in range(1, l + 1):
        visit[x][y + k] = 1
    return True

def heightUphill(x, y):
    if x - l < -1:
        return False
    for k in range(l - 1):
        if graph[x - k][y] != graph[x - k - 1][y]:
            return False
    for k in range(l):
        if visit[x - k][y] == 1:
            return False
    for k in range(l):
        visit[x - k][y] = 1
    return True

def heightDownhill(x, y):
    if x >= n - l:
        return False
    for k in range(1, l):
        if graph[x + k][y] != graph[x + k + 1][y]:
            return False
    for k in range(1, l + 1):
        if visit[x + k][y] == 1:
            return False
    for k in range(1, l + 1):
        visit[x + k][y] = 1
    return True

n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visit = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
    check = 0
    for j in range(n - 1):
        if graph[i][j] == graph[i][j + 1]:
            continue
        elif graph[i][j] + 1 == graph[i][j + 1]:
            if widthUphill(i, j) == False:
                check = 1
                break
        elif graph[i][j] - 1 == graph[i][j + 1]:
            if widthDownhill(i, j) == False:
                check = 1
                break
        else:
            check = 1
            break
    if check == 0:
        cnt += 1

visit = [[0] * n for _ in range(n)]
for j in range(n):
    check = 0
    for i in range(n - 1):
        if graph[i][j] == graph[i + 1][j]:
            continue
        elif graph[i][j] + 1 == graph[i + 1][j]:
            if heightUphill(i, j) == False:
                check = 1
                break
        elif graph[i][j] - 1 == graph[i + 1][j]:
            if heightDownhill(i, j) == False:
                check = 1
                break
        else:
            check = 1
            break
    if check == 0:
        cnt += 1

print(cnt)