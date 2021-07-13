import sys

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

ans = 10 ** 10
num1, num2, num3 = 0, 0, 0

for i in range(n - 2):
    if i > 0 and liquid[i] == liquid[i - 1]:
        continue
    left, right = i + 1, n - 1

    while left < right:
        sum = liquid[i] + liquid[left] + liquid[right]

        if abs(sum) < abs(ans):
            num1 = liquid[i]
            num2 = liquid[left]
            num3 = liquid[right]
            ans = sum

        if sum < 0:
            left += 1
        elif sum > 0:
            right -= 1
        else:
            print(liquid[i], liquid[left], liquid[right])
            sys.exit(0)

print(num1, num2, num3)