# [백준 1260번] DFS와 BFS

- **문제 링크** : [DFS와 BFS](https://boj.kr/1260)
- **난이도** : 실버2
- **풀이 날짜** : 2025-02-10
---

## 📖 문제 설명

> 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 📌 입력

> 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

## 📌 출력

> 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

## ⌨️ 예제 입출력
### 입력

```python

```
### 출력

```python

```

---

## 📝 풀이 코드

```python
from collections import defaultdict, deque
from queue import PriorityQueue
import sys
import math
sys.setrecursionlimit(10000)
input = sys.stdin.readline


N,M,V = map(int,input().split()) # 노드, 엣지, 시작 노드

A = [[] for _ in range (N+1)] # 인접행렬 리스트

dfs_visited = [False] * (N+1) # 방문
bfs_visited = [False] * (N+1)


# 인접행렬 초기화
for _ in range(M):
    s,e = map(int,input().split()) 
    A[s].append(e)
    A[e].append(s)

for i in range(len(A)): # DFS 와 BFS 순서를 보장하기 위해 정렬
    A[i].sort()

# DFS
def dfs(node):
    print(node, end=" ")
    dfs_visited[node] = True
    for i in A[node]:
        if not dfs_visited[i]:
            dfs(i)

dfs(V)

print()



def bfs(node):
    queue = deque()
    queue.append(node)
    bfs_visited[node] = True
    while queue:
        now_node = queue.popleft()
        print(now_node, end=" ")
        for i in A[now_node]:
            if not bfs_visited[i]:
                bfs_visited[i] = True
                queue.append(i)

bfs(V)
```

---
 
### 🔍 코드 설명
- N : 노드
- M : 엣지  
- V : 시작 노드
- DFS와 BFS 사용한 탐색
- 방문 순서를 보장하기 위해 정렬(오름차순)
- DFS : 재귀 사용
- BFS : Queue 사용
