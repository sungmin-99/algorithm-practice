# 백트래킹

-------------
## 1) 정의
> 해를 찾아가는 도중, 지금의 경로가 해가 될 것 같지 않으면 그 경로를 더이상 가지 않고 되돌아간다.   
> 브루트포스와 헷갈리는 경우가 있지만 가지치기 할 수 있는 여지가 있다면 백트래킹이 훨씬 유리하다.
-------------
## 2) 문제
### [N-Queen](https://www.acmicpc.net/problem/9663)
크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
```python
import sys
input = sys.stdin.readline

def solution(x):
    if x == n:
        global cnt
        cnt += 1
    else:
        for i in range(n):
            if visited[i]:
                continue
                
            board[x] = i
            
            if check(n):
                visited[i] = True
                solution(x + 1)
                visited[i] = False
                
def check(x):
    for i in range(x):
        if (board[x] == board[i]) or (x - i == abs(board[x] = board[i])):
            return False
        
    return True

n = int(input())
cnt = 0
board = [0 for _ in range(n)]
visited = [False for _ in range(n)]

solution(0)
print(cnt)
```
