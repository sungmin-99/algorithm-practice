n ,k = map(int, input().split())
enemy = []
for _ in range(n):
    enemy.append(list(map(int, input().split())))
ans, ansA, ansB, ansC = 10**10, 10**10, 10**10, 10**10

for i in range(n):
    for j in range(n):
        for s in range(n):
            cnt = 0
            a = enemy[i][0]
            b = enemy[j][1]
            c = enemy[s][2]

            for l in range(n):
                if a >= enemy[l][0] and b >= enemy[l][1] and c >= enemy[l][2]:
                    cnt += 1
                if cnt >= k and a + b + c < ansA + ansB + ansC:
                    ansA = a
                    ansB = b
                    ansC = c

print(ansA + ansB + ansC)