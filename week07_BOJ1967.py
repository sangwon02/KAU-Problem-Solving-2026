import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))
    graph[v].append((u, weight))

def dfs(start):
    dist = [-1]*(n+1) # 탐색안한 노드의 거리는 일단 -1
    dist[start] = 0 # 자신의 위치는 0
    q = deque([start]) # 측정해봐야하는 노드들의 모음
    
    while q: # 없을때까지 반복
        cur = q.popleft()
        
        for x1, weight in graph[cur]: # 전부 돌아가면서
            if dist[x1] == -1: # 만약 탐색이 안되었다면
                dist[x1] = dist[cur] + weight # 갱신해주고
                q.append(x1)  # 다음 탐색해야하는 값 추가
                
    
    maxnum = max(dist[1:]) # 최대 거리 찾고
    index = dist.index(maxnum)  # 최대 거리 값이 되는 짝 노드 값을 찾아줌
    
    return index, maxnum


index1, no = dfs(1)
index2, res = dfs(index1)

print(res)