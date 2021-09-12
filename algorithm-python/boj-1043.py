import itertools
from collections import deque

def bfs(x):
    q = deque()
    q.appendleft(x)
    visit[x] = True
    while q:
        x = q.pop()
        for i in setGraph[x]:
            if visit[i]:
                continue
            q.appendleft(i)
            visit[i] = True

n, m = map(int, input().split())
true = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
partylist = [[] for _ in range(m)]

for i in range(m):
    party = list(map(int, input().split()))
    del party[0]
    partylist[i] = party
    per = list(itertools.combinations(party, 2))
    for j in per:
        a, b = j
        graph[a].append(b)
        graph[b].append(a)

setGraph = [[] for _ in range(n + 1)]

for i in range(n + 1):
    setGraph[i] = set(graph[i])

visit = [False] * (n + 1)
for i in range(1, true[0] + 1):
    bfs(true[i])

cnt = 0
for i in partylist:
    check = True
    for j in i:
        if visit[j] == True:
            check = False
    if check:
        cnt += 1
print(cnt)