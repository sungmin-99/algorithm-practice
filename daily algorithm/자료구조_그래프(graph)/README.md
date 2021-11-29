# 그래프

-------------
## 1) 정의
> 그래프는 정점과 간선으로 이루어진 자료구조이다.  
> 정점간의 관계를 표현하는 관계도라고 생각할 수도 있다.  
> 트리도 그래프의 일종이다.
-------------
<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcjbjPd%2FbtqKgF6OzSD%2FU0a7BKCpfJlhx1iJzwsEy1%2Fimg.png">
<ul>
<li>정점(vertice) : 노드라고도 하며 정점에는 데이터가 저장된다.</li>
<li>간선(edge) : 링크라고도 하며 노드간의 관계를 나타낸다.</li>
<li>인접 정점(adjacent vertec) : 간선에 의해 연결된 정점이다.</li>
<li>차수(degree) : 무방향 그래프에서 하나의 정점에서 인접한 정점의 수</li>
</ul>  

--------------
## 2) 구현

### 인접행렬 방식
<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F7RFhy%2FbtqKkOhoYiE%2FSE3IQP2q0g3xd34EQZkjM1%2Fimg.png">
그래프의 노드를 2차원 배열로 만든다. <br>
각 정점에서 인접한 정점이면 1을 아니면 0을 넣는다. <br>
대각선을 기준으로 대칭된 구조가 나타난다. <br>

구현하기는 쉽지만 O(n^2)으로 효율도 안좋은 편이고 2차원 배열로 많은 공간이 필요하기 때문에 자주 사용하지는 않는다.

<br><br><br>
### 인접리스트 방식
<img src = "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FNlh1G%2FbtqKicb2Wub%2FsHWVSS6bn2FZdijEJVR2r1%2Fimg.png">
그래프의 노드들을 리스트로 표현한다.<br>
파이썬에서는 2차원 리스트를 사용한다.<br>

구현이 비교적 어렵고 인접정점을 탐색하는 것이 비교적 느리지만 모든 인접정점을 탐색해야 하는 bfs, dfs 알고리즘에서 자주 이용한다.
