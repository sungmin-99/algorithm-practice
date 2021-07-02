n, a, d = map(int, input().split())
treble = list(map(int, input().split()))
cnt = 0
for i in range(len(treble)):
    if treble[i] == a + cnt * d:
        cnt += 1
print(cnt)