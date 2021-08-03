import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
tetro = [[[0, 1], [0, 2], [0, 3]],
        [[1, 0], [2, 0], [3, 0]],
        [[0, 1], [1, 0], [1, 1]],
        [[1, 0], [2, 0], [2, 1]],
        [[1, 0], [2, 0], [2, -1]],
        [[0, 1], [0, 2], [1, 0]],
        [[0, 1], [0, 2], [1, 2]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 1], [1, 0], [2, 0]],
        [[0, 1], [0, 2], [-1, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[1, 0], [1, 1], [2, 1]],
        [[1, 0], [1, -1], [2, -1]],
        [[0, 1], [-1, 1], [-1, 2]],
        [[0, 1], [1, 1], [1, 2]],
        [[0, 1], [0, 2], [1, 1]],
        [[1, 0], [1, 1], [2, 0]],
        [[1, 0], [1, -1], [2, 0]],
        [[0, 1], [0, 2], [-1, 1]]]

ans = 0
for i in range(n):
    for j in range(m):
        for tet in tetro:
            check = graph[i][j]

            for k in range(3):
                nx = i + tet[k][0]
                ny = j + tet[k][1]
                if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                    check += graph[nx][ny]

            if ans < check:
                ans = check

print(ans)