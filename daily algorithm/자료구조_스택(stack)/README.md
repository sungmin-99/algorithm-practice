# 스택(Stack)

-------------
## 1) 정의
> 데이터의 삭입과 삭제가 한쪽 방향에서만 일어나는 구조이다.   
> 나중에 삽입된 데이터가 먼저 삭제 되므로 <b> 후입선출(LIFO) </b> 구조라고도 한다.
-------------
## 2) 구현
python에서 ```list```로 스택구조를 구현합니다.  

<img src = "https://t1.daumcdn.net/cfile/tistory/2679DF3358881D3934">

이미지에서 보이는 ```push```는 ```append```함수를 이용하고 ```pop```은 ```pop```함수를 이용합니다.

- ```append``` : ```list``` 의 가장 마지막 ```index```에 요소를 삽입한다.   
- ```pop``` : ```list``` 의 가장 마지막 ```index```의 요소를 가져온다. ( ```list``` 에서는 삭제된다.)

<br>

> 스택에서 가장 기억해야 하는 것은 후입선출(LIFO) 이다.   
> 문제에서 나중에 삽입된 데이터를 먼저 사용하거나 삭제해야 한다면 Stack 사용을 염두해 두자


-----------

## 3) 예제
### [2019 카카오 개발자 겨울 인턴십 : 크레인 인형뽑기 게임](https://programmers.co.kr/learn/courses/30/lessons/64061)

<img src = "https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/8569d736-091e-4771-b2d3-7a6e95a20c22/crane_game_103.gif">

문제에서 인형이 들어있는 board의 상태와 집게가 인형을 집는 moves가 주어진다.   
그림과 같이 바구니에 인형을 넣었을 때 가장 TOP에 있는 인형과 같은 인형일 경우 두개 다 사라진다.

<b> 바구니에 넣는 과정에서 가장 TOP에 있는 요소를 사용하기 때문에 스택 구조임을 생각해야 한다. </b>

```python
def solution(board, moves):
    stacklist = [] # list로 스택을 구현
    answer = 0

    for i in moves:
        for j in range(len(board)): # 인형이 몇개가 쌓여 있는지 모르기 때문에 가장 위에부터 탐색한다.
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]: # 가장 위에 있는 요소 2개가 같다면 pop을 이용해 삭제한다.
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
```
> 제목은 스택문제로 하겠습니다. 근데 이제 구현을 곁들인

2차원 ```list``` 를 이용해 board를 구현한 문제라서 사용해보지 않았다면 생소할 수 있지만 2차원 ```list```는 많은 자료구조와 알고리즘에 사용되기 때문에 미리 익숙해지는 것이 좋다.