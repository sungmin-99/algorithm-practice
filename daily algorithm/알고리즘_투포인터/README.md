# 투포인터

-------------
## 1) 정의
> 1차원 배열이 있고 이 배열에서 각자 다른 원소를 가리키고 있는 2개의 포인터를 조작해 원하는 값을 찾는다.   
> 이진탐색에서 주로 이용한다.
-------------
## 2) 문제
### [수들의 합](https://www.acmicpc.net/problem/2003)
```python
N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= N and left <= right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)

    if total == M:
        cnt += 1

        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(cnt)
```