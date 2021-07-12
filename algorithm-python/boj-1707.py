from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    visit[x] = 1
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                visit[i] = -visit[x]
                q.append(i)
            else:
                if visit[i] == visit[x]:
                    return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    ans = True
    graph = [[] for _ in range(v + 1)]
    visit = [0] * (v + 1)
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, v + 1):
        if visit[i] == 0:
            if not bfs(i):
                ans = False
                break
    if ans:
        print("YES")
    else:
        print("NO")