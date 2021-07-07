import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(x):
    dp[x] = 1
    for node in graph[x]:
        if not dp[node]:
            dfs(node)
            dp[x] += dp[node]
    return

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

for _ in range(q):
    q = int(input())
    print(dp[q])