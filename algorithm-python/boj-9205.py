t = int(input())

for _ in range(t):
    n = int(input())
    homeX, homeY = map(int, input().split())
    beerX, beerY = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        beerX.append(x)
        beerY.append(y)
    festivalX, festivalY = map(int, input().split())
    ans = True
    for i in range(n):
        if abs(homeX - beerX[i]) + abs(homeY - beerY[i]) > 1000:
            ans = False
        else:
            homeX, homeY = beerX[i], beerY[i]
    if abs(homeX - festivalX) + abs(homeY - festivalY) > 1000:
        ans = False

    if ans:
        print("happy")
    else:
        print("sad")