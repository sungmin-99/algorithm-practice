n = int(input())
arr = list(map(int,input().split()))
arr.sort()
a = n // 2
b = n % 2
print(arr[a+b-1])