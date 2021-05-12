n = int(input())
person = []
for _ in range(n):
    person.append(list(map(int,input().split())))
for i in range(n):
    cnt = 1
    for j in range(n):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            cnt += 1
    print(cnt,end=" ")