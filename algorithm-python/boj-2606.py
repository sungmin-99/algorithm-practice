def dfs(x):
    if virus[graph[x][0]] == 1:
        virus[graph[x][1]] = 1
    elif virus[graph[x][1]] == 1:
        virus[graph[x][0]] = 1
    return

n = int(input())
connect = int(input())
virus = [0] * (n + 1)
virus[1] = 1
graph = []
for _ in range(connect):
    graph.append(list(map(int,input().split())))
for _ in range(connect):       #시간복잡도 최악이지만 n의 값이 작아 문제는 없다...
    for i in range(connect):
         dfs(i)
print(virus.count(1)-1)