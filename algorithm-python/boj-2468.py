import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x + 1,y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    else:
        return False

n = int(input())
graph1 = []
for _ in range(n):
    graph1.append(list(map(int,input().split())))

minx, maxx = 101, 0
for i in range(n):
    minx = min(minx,min(graph1[i]))
    maxx = max(maxx,max(graph1[i]))

graph = []
for i in range(n):
    graph.append([0] * n)

ans = 0
for i in range(minx, maxx+1):
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph1[j][k] >= i:
                graph[j][k] = 1
            else:
                graph[j][k] = 0
    for j in range(n):
        for k in range(n):
            if dfs(j,k) == True:
                cnt += 1
    ans = max(cnt,ans)
print(ans)