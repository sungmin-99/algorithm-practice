# 큐(queue), 덱(deque)

-------------
## 1) 정의
> 큐(queue) 구조는 스택과는 다르게 먼저 집어 넣은 데이터가 먼저 나오는 FIFO(First In First Out) 이다.   
> 현실에서 줄을 서거나 번호표를 뽑는 경우처럼 가장 많이 볼 수 있는 형태이다.   
> 덱(deque) 구조는 데이터의 삭제와 삽입이 앞뒤 모두 이뤄질 수 있다.
-------------
## 2) 구현
<img src = "https://media.vlpt.us/images/choiiis/post/582bdddb-e130-4f0f-8fc4-5e5b23a6d1b3/image.png">
<br>
큐(queue)와 덱(deque)을 직관적으로 이해하는 것은 어렵지 않다. <br>
하지만 구현에서 스택과 차이를 가진다. <br>

덱이나 큐 구조를 ```list``` 를 이용해서도 구현 할 수 있지만 매우 비효율적이다.   
같은 이유로 ```python```에서는 큐(queue)를 구현할 때도 덱(deque)의 모듈을 사용한다.

```python 
from collections import deuqe
```
```list``` 에는 없는 ```appendleft```와 ```popleft``` 메서드를 지원한다.

```q.appendleft(x)``` : q의 앞쪽에 요소를 추가한다.   
```q.append(x)``` : q의 뒤쪽에 요소를 추가한다.   
```q.popleft(x)``` : q의 앞쪽의 요소를 가져온다.   
```q.pop(x)``` : q의 뒤쪽의 요소를 가져온다.   
    
사용법은 ```list```에서 메소드가 추가된 정도라 어렵지 않다.

-------------
## 3) 예제
### [요세푸스 문제](https://www.acmicpc.net/problem/1158)

문제에서 N과 K가 주어진다.   
N명의 사람들이 원을 이루며 앉아있고 K번째 사람을 제거한다. 계속해서 K번째 사람을 제거하면서 제거되는 순서가 요세푸스 순열이다.   
N과 K가 주어지면 요세푸스 순열을 정답을 출력한다.

```python
from collections import deque

n, k = map(int,input().split())
arr = deque()
ans = []
for i in range(1,n+1):
    arr.append(i)
while arr:
    for _ in range(k-1):
        a = arr.popleft()
        arr.append(a)
    ans.append(arr.popleft())
    
print("<",end="")
for i in range(n-1):
    print(ans[i],end=", ")
print(f"{ans[-1]}>")
```

사람들이 원으로 앉아 있다고 생각하면 큐 구조를 떠올리기 쉽지 않다.   
> 하지만 먼저 들어온 사람이 먼저 나가는 큐 구조에서 출구와 입구를 연결하면 원형이 된다.   

큐와 덱 또한 우선순위 큐나 BFS탐색을 할 때 꼭 필요한 자료구조 이다.