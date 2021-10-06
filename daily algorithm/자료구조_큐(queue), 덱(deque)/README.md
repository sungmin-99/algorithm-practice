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
```list```