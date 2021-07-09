from sys import stdin

n, k = map(int, input().split())
arr = list(map(int, stdin.readline().split()))

def answer():
    global n, k, arr
    startIndex, maxCount = (0, 0)
    cnt = [0] * 100001
    for i in range(len(arr)):
        num = arr[i]
        cnt[num] = cnt[num] + 1
        if cnt[num] > k:
            maxCount = max(maxCount, i - startIndex)
            while (cnt[num] > k):
                cnt[arr[startIndex]] = cnt[arr[startIndex]] - 1
                startIndex += 1
        else:
            maxCount = max(maxCount, i - startIndex + 1)
    return maxCount

print(answer())