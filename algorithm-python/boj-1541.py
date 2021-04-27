n = list(input().split("-"))
if n[0] == '': # -로 시작하는 경우 NULL 값이 들어가 런타임 에러를 방지
    n[0] = '0'
ans = 0
for i in range(len(n)):
    ans -= sum(map(int,n[i].split("+")))
print(ans + sum(map(int,n[0].split("+"))) * 2)