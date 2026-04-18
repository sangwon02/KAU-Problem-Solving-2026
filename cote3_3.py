import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)] # 그래프로 담아둠
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    
having = {1}

def BFS():
    queue = deque([1]) # 교환할 아이템을 담는 큐 일단 1로
    while queue:
        check = queue.popleft() # 교환할 아이템을 꺼냄
        
        for i in graph[check]: # 교환 가능한게 있는지 확인
            if i not in having: # 교환이 가능하고 처음 얻는 아이템이면
                having.add(i) # 얻을 수 있음
                queue.append(i) # 다음 교환할 아이템에 추가
                
BFS()

print(len(having))
