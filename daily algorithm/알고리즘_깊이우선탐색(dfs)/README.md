# 깊이우선탐색 (dfs)

-------------
## 1) 정의
> Depth First Search의 약자로 이름과 같이 깊이우선탐색이다.   
> 트리나 그래프에서 한 루트로 더이상 탐색할 수 없을 때까지 탐색하다가 더이상 탐색할 수 없으면 이전으로 돌아와서 계속한다.   
> 기본적으로 재귀를 통한 스택구조를 가진다.    

-------------
## 2) 구현
<img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Depth-First-Search.gif/330px-Depth-First-Search.gif">   

그림과 같이 더이상 탐색할 수 없는 깊이까지 탐색한 후 돌아온다.   
재귀 구조를 가지며 자연스럽게 스택이 형성되어 가장 나중에 들어온 노드를 가장 먼저 탐색한다.   
좀더 자세히 구현 순서를 분석해보면   
> 1. 처음 1번노드를 탐색할 때 스택에 ```[9, 5, 2]``` 가 들어온다.   
> 2. 스택구조이므로 다음 2번 노드를 탐색할 때 ```[9, 5, 3]``` 이 된다.
> 3. 다음으로 처음에 들어왔던 5번과 9번 노드는 뒤로 재쳐두고 3번노드를 탐색한다. ```[9, 5, 4]``` 
> 4. 4번노드를 탐색할 땐 스택아 아무것도 들어오지 않는다. ```[9, 5]```
> 5. 더 이상 탐색할 노드가 없으니 처음 들어왔던 5번 노드로 돌아간다. ```[9, 8, 6]```
> 6. 6번노드를 탐색하면 7번 노드가 들어온다. ```[9, 8, 7]```
> 7. 7번노드가 단말노드 이므로 8번노드로 돌아온다. ```[9, 8]```
> 8. 8번노드도 단말 노드이므로 9번노드로 돌아온다. ```[9]```
> 9. 9번노드를 탐색하며 10번노드가 들어온다. ```[10]```
> 10. 10번노드를 탐색하면 더 이상 스택에 남아있는 노드가 없으므로 dfs를 종료한다.

### 구현이 비교적 쉽다는 장점이 있지만 bfs보다 속도가 느리고 최단거리를 구하는 것이 불가능하다.
### 때문에 그래프 탐색 문제에서 dfs를 사용할지 bfs를 사용할지 결정하는 것도 중요하다.

-----------------
## 3) 예제
### [섬의 개수](https://www.acmicpc.net/problem/4963)

<img src = "https://www.acmicpc.net/upload/images/island.png">

그래프에 1과 0으로 섬과 바다가 표시된다. 그 중 섬끼리 상하좌우대각선중 하나라도 붙어있으면 같은섬이다.   
문제에서 섬의 개수가 몇개인지 찾아낸다.

```python
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x, y+1)
        dfs(x+1, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x-1, y-1)
        dfs(x+1, y-1)
        dfs(x-1, y+1)
        return True
    return False

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int,input().split())))
    result = 0
    for i in range(w):
        for k in range(h):
            if dfs(k, i) == True:
                result += 1
    print(result)
```

문제의 접근 방법은 간단하다. 모든 노드를 탐색해서 바다이면 다음으로 넘어가고 육지이면 dfs로 붙어있는 섬을 지워버린다.   
<b>dfs문제의 경우 틀이 대부분 비슷하기 때문에 큰 틀을 파악하고 상황에 맞게 응용하는 것이 중요하다.</b>