from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    xcnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0:
                ny = m-1
            elif ny > m-1:
                ny = 0

            if 0 <= nx < n and 0 <= ny < m and not c[nx][ny]:
                if a[x][y] == a[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
                    xcnt += 1
    return xcnt

n, m, t = map(int, input().split())

a, nsum, nm = [], 0, n*m
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    nsum += sum(row)

q = deque()
c = [[0] * m for _ in range(n)]

for _ in range(t):
    x, d, k = map(int, input().split())

    k %= m
    for i in range(x-1, n, x):
        if d == 0:
            a[i] = a[i][-k:] + a[i][:-k]
            c[i] = c[i][-k:] + c[i][:-k]
        else:
            a[i] = a[i][k:] + a[i][:k]
            c[i] = c[i][k:] + c[i][:k]

    flag = 0
    for i in range(n):
        for j in range(m):
            if not c[i][j]:
                cnt = bfs(i, j)
                if cnt:
                    nsum -= a[i][j] * cnt
                    nm -= cnt
                    flag = 1

    if nm == 0:
        print(0)
        sys.exit()

    if not flag:
        avg = nsum / nm
        for i in range(n):
            for j in range(m):
                if not c[i][j]:
                    if a[i][j] > avg:
                        a[i][j] -= 1
                        nsum -= 1
                    elif a[i][j] < avg:
                        a[i][j] += 1
                        nsum += 1
print(nsum)