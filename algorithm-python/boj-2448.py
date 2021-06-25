def printStar(x, y, n):
    if n == 3:
        star[x][y] = '*'
        star[x + 1][y - 1], star[x + 1][y + 1] = '*', '*'
        for i in range(-2, 3):
            star[x + 2][y + i] = '*'
    else:
        printStar(x, y, n // 2)
        printStar(x + n // 2, y - n // 2, n // 2)
        printStar(x + n // 2, y + n // 2, n // 2)

n = int(input())
star = [[' '] * 2 * n for _ in range(n)]

printStar(0, n - 1, n)
for i in star:
    print("".join(i))