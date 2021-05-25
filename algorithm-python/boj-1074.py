n, r, c = map(int, input().split())
size = 2 ** n
ans = 0
while size != 1:
    if r < size // 2 and c < size // 2: # 1
        size = size // 2
    elif r < size // 2 and c >= size // 2: # 2
        ans += (size // 2) ** 2
        c -= size // 2
        size = size // 2
    elif r >= size // 2 and c >= size // 2: # 3
        c -= size // 2
        r -= size // 2
        ans += ( (size // 2) ** 2 ) * 3
        size = size // 2
    else: # 4
        r -= size // 2
        ans += ( (size // 2) ** 2 ) * 2
        size = size // 2
print(ans)