from collections import deque
import sys

T = int(sys.stdin.readline())

errFlag = False
for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].split(",")

    if arr[0] != '':
        arr = deque(arr)
    else:
        arr = deque()

    direction_Flag = True

    for i in p:
        if i == "R":
            if direction_Flag == True:
                direction_Flag = False
            elif direction_Flag == False:
                direction_Flag = True
        elif i == "D":
            if len(arr) == 0:
                print("error")
                errFlag = True
                break

            if direction_Flag == True:
                arr.popleft()
            elif direction_Flag == False:
                arr.pop()

    if p.count('R') % 2 != 0:
        arr.reverse()

    if errFlag == False:
        print("[", end="")
        for i in range(len(arr)):
            print(arr[i], end="")
            if i != len(arr) - 1:
                print(",", end="")
        print("]")
    errFlag = False