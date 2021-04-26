n = int(input())
sequence = list(map(int,input().split()))
sequence.sort()
ans = [0] * 1001
for i in range(n):
    ans[i] = sum(sequence[:i+1])
print(sum(ans))