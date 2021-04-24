import sys
sys.setrecursionlimit(1000000) #재귀가 1000을 넘어가므로 런타임 에러가 발생한다.
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append([0 for x in range(m)])
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    check = 0
    for i in range(n):
        for k in range(m):
            if dfs(i,k) == True:
                check += 1
    print(check)