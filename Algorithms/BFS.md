# BFS(너비 우선 탐색)
```python
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
```

## 큐를 이용한 반복 구조

모든 인접 간선을 추출하고 도착점인 정점을 큐에 삽입

```python
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
```
```python
discovered = [1, 2, 3, 4, 5, 6, 7]
```

### collections.deque를 이용한 최적화

```python
import collections

def iterative_bfs(start_v):
    discovered = [start_v]
    queue = collections.deque([start_v])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
```

그래프가 작아서 그런지 최적화하기 전 코드가 더 빨리 실행되는데, 노드와 간선의 수가 많아지면 최적화한 코드가 더 빨라질 거 같음

## 재귀 구현 불가
```
💡 BFS는 재귀로 구현할 수 없다
```