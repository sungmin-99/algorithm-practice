import sys
from collections import deque
input = sys.stdin.readline #입력이 많아 그냥 input을 사용하면 시관초과가 나옴
q = deque()
def push(q,x):
    return q.append(int(x))

def pop(q):
    if len(q) != 0:
        return print(q.popleft())
    else:
        return print("-1")

def size(q):
    return print(len(q))

def empty(q):
    if len(q) == 0:
        print("1")
    else:
        print("0")
    return

def front(q):
    if len(q) == 0:
        return print("-1")
    else:
        return print(q[0])

def back(q):
    if len(q) == 0:
        return print("-1")
    else:
        return print(q[-1])


n = int(input())
for i in range(n):
    comand = list(input().split())
    if comand[0] == 'push':
        push(q,comand[1])
    elif comand[0] == 'pop':
        pop(q)
    elif comand[0] == 'size':
        size(q)
    elif comand[0] == 'empty':
        empty(q)
    elif comand[0] == 'front':
        front(q)
    else:
        back(q)