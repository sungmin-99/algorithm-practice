n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
sensor.sort()
distance = []
if k >= n:
    print("0")
else:
    for i in range(n-1):
        distance.append(sensor[i+1] - sensor[i])
    for _ in range(k-1):
        distance.remove(max(distance))
    print(sum(distance))