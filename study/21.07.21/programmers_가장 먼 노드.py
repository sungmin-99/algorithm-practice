from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    visit = [0] * (n + 1)

    q = deque()
    q.appendleft(1)
    visit[1] = 1
    while q:
        x = q.pop()
        for i in graph[x]:
            if visit[i] == 0:
                q.appendleft(i)
                visit[i] = visit[x] + 1
                ans = visit[x] + 1
    cnt = 0
    for i in range(len(visit)):
        if visit[i] == ans:
            cnt += 1
    return cnt