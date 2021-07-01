def nextPermutations(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    ans = arr[:i + 1]
    ans.extend(list(reversed(arr[i + 1:])))
    return ans

t = int(input())
for _ in range(t):
    word = list(input())
    ans = nextPermutations(word)
    if not ans:
        print("".join(word))
    else:
        print("".join(ans))