n = int(input())
arrRoad = list(map(int,input().split()))
arrCity = list(map(int,input().split()))
i, result = 0, 0
while i != n - 1:
    for k in range(i,n):
        if arrCity[i] > arrCity[k]:
            result += arrCity[i] * sum(arrRoad[i:k])
            i = k
            break
        elif k == n-1:
            result += arrCity[i] * sum(arrRoad[i:k])
            i = k
print(result)