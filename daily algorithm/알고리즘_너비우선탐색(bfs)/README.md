# 너비우선탐색 (bfs)

-------------
## 1) 정의
> Breadth First Search의 약자로 이름과 같이 깊이우선탐색이다.  
> dfs와 유사한 구조를 가지고 있지만 탐색하는 방법에서 차이가 있다.   
> 큐(queue) 구조를 이용해 먼저 들어온 간선을 먼저 탐색한다.

-------------
## 2) 구현
<img src = "https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif">

예제에서 볼 수 있겠지만 ```deque``` 을 이용한 ```queue``` 구조로 구현한다.      
먼저 들어온 노드를 먼저 탐색하므로 루트노드에서 부터의 거리를 구할 수 있다.   
dfs에서 재귀구조를 사용하는 것과 반대로 ```while```을 사용하므로 더 효율적이다.

-------------

## 3) 예제
### [미로탐색](https://www.acmicpc.net/problem/2178)

1과 0으로 표현된 미로가 있다. 1은 이동 할 수 있는 칸이고 0은 이동할 수 없는칸이다.
(1, 1) 위치에서 출발해 (N, M) 위치로 이동할 때 최단거리를 구하여라

```python
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

    return graph[n-1][m-1]

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,list(input()))))

print(bfs(0,0))
```

문제에 최단거리나 칸수를 구하여라 같은 문장이 나오면 dfs는 바로 배제하는 것이 좋다.   
```from collections import deque```을 사용해 queue 구조를 이용한다.