n = int(input())
price = []
for _ in range(n):
    price.append(int(input()))
price.sort(reverse=True)
ans = sum(price)
for i in range(2,(n//3)*3,3):
    ans -= price[i]
print(ans)