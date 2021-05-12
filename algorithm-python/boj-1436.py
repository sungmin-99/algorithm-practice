n = int(input())
serise = 666
cnt = 0
while True:
    if '666' in str(serise):
        cnt += 1
    if cnt == n:
        print(serise)
        break
    serise += 1