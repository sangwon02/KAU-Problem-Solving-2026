from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    n, m = map(int, input().split())
    # 정보 입력 받음
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    # 방문 여부 및 밟은 블록 개수를 저장할 리스트
    visited = [[0] * m for _ in range(n)]
    
    # 시작점 (0, 0) 큐에 삽입 및 방문 처리
    queue = deque([(0, 0)])
    visited[0][0] = 1
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while queue:
        x, y = queue.popleft()
        
        # 출구에 도착하면 누적된 블록 개수 반환 후 종료
        if x == n - 1 and y == m - 1:
            return visited[x][y]
            
        # 4방향으로 이동 시도
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 넘지 않고 방문한 곳이 아니면 탐색
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                # 현재 블록과 다음 블록의 높이 차이가 1 이하이면 이동
                if abs(grid[nx][ny] - grid[x][y]) <= 1:
                    visited[nx][ny] = visited[x][y] + 1  # 이전 블록 개수 + 1 최신화
                    queue.append((nx, ny))
                    
    # 답이 없는 경우
    return 0

print(BFS())