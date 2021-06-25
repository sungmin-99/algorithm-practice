def dfs(x):
    cnt = 0
    visit[x] = 1
    for i in range(n):
        if graph[x][i] == 1 and visit[i] == 0:
            cnt += dfs(i)
    if cnt == 0:
        cnt += 1
    return cnt

n = int(input())
node = list(map(int, input().split()))
removeNode = int(input())
graph = [[0] * n for _ in range(n)]
visit = [0] * (n + 1)
for i in range(len(node)):
    if node[i] != -1:
        graph[i][node[i]] = 1
        graph[node[i]][i] = 1
graph[removeNode][node[removeNode]] = 0
graph[node[removeNode]][removeNode] = 0

rootNode = node.index(-1)
if rootNode == removeNode:
    print("0")
else:
    print(dfs(rootNode))