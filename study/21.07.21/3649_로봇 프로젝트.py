import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * (10 ** 7)
        n = int(input())
        legos = []
        for _ in range(n):
            legos.append(int(input()))
        start, end = 0, n - 1
        legos.sort()
        check = True

        while start < end:
            if legos[start] + legos[end] == x:
                print(f"yes {legos[start]} {legos[end]}")
                check = False
                break
            elif legos[start] + legos[end] < x:
                start += 1
            else:
                end -= 1

        if check:
            print("danger")
    except:
        break