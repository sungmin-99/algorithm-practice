# 이분탐색

-------------
## 1) 정의
> 이미 정렬되어 있는 배열에서 탐색 범위를 반씩 줄여가며 찾고자 하는 값을 탐색하는 방법.
> 배열을 순차대로 탐색할 경우보다 시간복잡도가 훨씬 유리하다 
-------------

## 2) 구현
1. 배열을 정렬한다
2. 정렬된 배열에서 시작 ```start``` 끝 ```end``` 중간 ```mid```를 할당한다
3. ```mid```의 값과 ```target```을 비교한다.
   1. ```mid``` 값 보다 ```target``` 이 크면 ```start = mid + 1```
   2. ```mid``` 값 보다 ```target``` 이 작으면 ```end = mid - 1```
4. ```target``` 이 없으면, ```None```을 반환

```python
#반복
def binary_search(array, target):
    array.sort() # 정렬
    
    left = 0
    right = len(array)-1
    
    while left <= right:
        mid = (left + right)//2 # 가운데 인덱스
        if array[mid] == target: # 찾는 값을 만나면 반환
            return mid 
        elif array[mid] > target: # 가운데 값이 더 크면 왼쪽 구간으로 이동
            right = mid-1 
        else: # 가운데 값이 더 작으면 오른쪽 구간으로 이동
            left = mid+1
    
    return None # 찾는 값이 없을 때
```

```python
#재귀
def binary_search(array, target, left, right):
    
    if left > right: # 찾는 값이 없을 때
        return None
    
    mid = (left + right)//2
    if target == array[mid]:
        return
    elif target > array[mid]: # 왼쪽 구간에 대해 재귀 호출
        binary_search(array, target, left, mid-1)
    else: # 오른쪽 구간에 대해 재귀 호출
        binary_search(array, target, mid+1, right) 
```

-------------

## 3) 문제
### [랜선 자르기](https://www.acmicpc.net/problem/1654)