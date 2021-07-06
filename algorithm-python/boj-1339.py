n = int(input())
words = []
for _ in range(n):
    words.append(input())

dic = {}
for word in words:
    k = len(word) - 1
    for a in word:
        if a in dic:
            dic[a] += pow(10, k)
        else:
            dic[a] = pow(10, k)
        k -= 1

nums = []
for value in dic.values():
    nums.append(value)
nums.sort(reverse = True)
ans, n = 0, 9

for i in range(len(nums)):
    ans += nums[i] * n
    n -= 1

print(ans)