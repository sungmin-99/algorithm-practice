def quad(x, y, n):
    if n == 1:
        return graph[x][y]
    ans = ''
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != graph[x][y]:
                ans = ans + '('
                ans = ans + quad(x, y, n // 2)
                ans = ans + quad(x, y + n // 2, n // 2)
                ans = ans + quad(x + n // 2, y, n // 2)
                ans = ans + quad(x + n // 2, y + n // 2, n // 2)
                ans = ans + ')'
                return ans
    return graph[x][y]

t = int(input())
graph = []
for _ in range(t):
    graph.append(input())

print(quad(0, 0, t))