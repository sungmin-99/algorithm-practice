# 1. 연속되는 수가 나올 것
# 2. 뒤의 수의 개수가 앞의 수보다 크면 안됨
# 3. 같은 숫자는 3개이상 나오면 안됨
# 4. 가장 큰숫자가 1개일 경우 경우의 수 *2를 해줄 것

n = int(input())
arr = list(map(int, input().split()))
total = [0] * 41
check = 2

for i in arr:
    total[i] += 1

tmp = True
for cnt in total:
    if cnt > check:
        tmp = False
        break
    check = cnt

if tmp:
    print(2 ** (total.count(2) + (1 if 1 in total else 0)))
else:
    print(0)