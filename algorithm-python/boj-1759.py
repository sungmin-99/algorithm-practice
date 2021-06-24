from itertools import combinations

l, c = map(int, input().split())
letter = sorted(list(input().split()))
passwd = list(combinations(letter, l))

for i in passwd:
    check = 0
    for j in i:
        if j in 'aeiou':
            check += 1

    if 1 <= check <= l-2:
        print(''.join(i))