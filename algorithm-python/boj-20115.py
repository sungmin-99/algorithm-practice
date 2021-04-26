n = int(input())
arrDrink = list(map(int,input().split()))

ans = max(arrDrink)
arrDrink.remove(max(arrDrink))
ans += sum(arrDrink) / 2
print(ans)