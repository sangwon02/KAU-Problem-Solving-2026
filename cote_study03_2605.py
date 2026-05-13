from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    # 일단 정보 입력 받아 2차원 리스트에 저장
    grid = [list(map(int, input().split())) for _ in range(7)]
    
    # 방문 여부 담을 곳
    visited = [['0']*7 for _ in range(7)]
    
    # 상하좌우 탐색용 리스트
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 답을 담을 변수
    result = 0
    
    # 모두 다 돌면서 탐색
    for i in range(7):
        for j in range(7):
            # 탐색했는지 안했는지 확인 후에 탐색
            if visited[i][j] == '0':
                # 탐색을 위한 대기열에 넣어줌
                queue = deque([(i, j)])
                
                # 해당 좌표 탐색했다고 바꿔줌
                visited[i][j] = '1' 
                
                # 현재 색깔을 담아주고
                color = grid[i][j]
                
                # 현재 탐색중인 것에 연결된거
                cnt = 1
                
                # 대기열이 다 쓰일때까지 탐색
                while queue: 
                    # 대기열에서 좌표 꺼내줌
                    x, y = queue.popleft()
                    
                    # 해당 좌표에서 상하좌우 탐색
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        # 넘어가지 않는지 확인해주고
                        if 0 <= nx < 7 and 0 <= ny < 7:
                            # 방문하지 않고 현재 색깔과 같은 부분이 있다면
                            if visited[nx][ny] == '0' and grid[nx][ny] == color:
                                visited[nx][ny] = 1 # 방문했다고 표시해주고
                                queue.append((nx,ny)) # 다음 탐색을 위한 대기열에 넣어줌
                                cnt += 1
                                
                if cnt >= 3: # 연결된게 3개 이상이면
                    result += 1 # 정답 개수 +1
    return result
                
                

print(BFS())
    
    
