import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000000000)

M, N = map(int, input().split())


dy = [-1, 1, 0, 0] 
dx = [0, 0, -1, 1]    
    

arr = []

for _ in range(M):
    row = [int(num) for num in input().strip()]
    arr.append(row)

check = [[0]*N for _ in range(M)] # 가봤는지 안가봤는지 체크

def dfs(y, x):
    check[y][x] = 1
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if ny < 0 or ny >= M or nx < 0 or nx >= N: # 벗어나면 안되는 거
            continue
        if arr[ny][nx] == 1: # 가봤는지 안가봤는지 체크
            continue
        if check[ny][nx] == 1: # 막힌거면 패스
            continue
        
        dfs(ny, nx)
        
for i in range(N):
    if arr[0][i] == 0 and check[0][i] == 0: # 만약 뚫려 있고 체크 안한곳만 탐색 시작
        dfs(0, i)
        
for i in range(N):
    if check[-1][i] == 1:
        print("YES")
        exit()

print("NO")
    