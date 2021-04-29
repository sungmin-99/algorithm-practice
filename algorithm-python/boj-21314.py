mk = input()
maxans = ''
minans = ''
stack = 0

for i in range(len(mk)):
    if mk[i] == 'M':
        stack += 1
    elif mk[i] == 'K':
        maxans = maxans + str(5 * (10 ** stack))
        stack = 0
if stack != 0:
    maxans = maxans + ('1' * stack)
    stack = 0
print(maxans)

for i in range(len(mk)):
    if mk[i] == 'M':
        stack += 1
    if mk[i] == 'K':
        if stack == 1:
            minans = minans + '1' + '5'
        elif stack > 1:
            minans = minans + str(10 ** (stack - 1)) + '5'
        elif stack == 0:
            minans = minans + '5'
        stack = 0
if stack != 0:
    minans = minans + str(10 ** (stack - 1))
    stack = 0
print(minans)