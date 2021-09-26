import heapq
import sys
input = sys.stdin.readline
INF = 1e9

def MST(x):
    q = []
    heapq.heappush(q, (0, x))
    while q:
        dist, computer = heapq.heappop(q)
        if distance[computer] != INF:
            continue
        distance[computer] = dist
        for i in graph[computer]:
            heapq.heappush(q, (i[1], i[0]))

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

distance = [INF] * (n + 1)
MST(1)
del distance[0]
print(sum(distance))