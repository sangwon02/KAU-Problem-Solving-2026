# 백준 11725
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

# 트리의 간선 정보 입력받기
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 부모를 저장할 배열 (0이면 아직 방문하지 않음을 의미)
parent = [0] * (n + 1)

def bfs():
    # 루트 노드인 1번부터 탐색 시작
    queue = deque([1])
    parent[1] = 1  # 1번 노드 방문 처리 (루트 노드)
    
    while queue:
        current = queue.popleft()
        
        # 현재 노드와 연결된 모든 노드를 확인
        for next_node in graph[current]:
            if parent[next_node] == 0:  # 아직 방문하지 않은 노드라면
                parent[next_node] = current  # 현재 노드가 부모가 됨
                queue.append(next_node)

bfs()

for i in range(2, n + 1):
    print(parent[i])