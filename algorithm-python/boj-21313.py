n = int(input())

if n % 2 == 0:
    for i in range(n // 2):
        print("1 2", end = " ")
else:
    for i in range(n // 2):
        print("1 2", end=" ")
    print("3")