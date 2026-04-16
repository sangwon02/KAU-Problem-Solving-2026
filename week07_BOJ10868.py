import sys
import math
input = sys.stdin.readline

# [1단계] 입력
N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
# [2단계] 블록 나누기
block_size = int(math.sqrt(N)) + 1
num_blocks = (N + block_size - 1) // block_size
# [3단계] 전처리 - 각 블록의 최솟값
block_min = [float('inf')] * num_blocks
for i in range(N):
    b = i // block_size
    if A[i] < block_min[b]:
        block_min[b] = A[i]
# [4단계] 질의 처리
result = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1   # 0-indexed로 변환
    b -= 1
    
    ans = float('inf')
    start_block = a // block_size
    end_block = b // block_size
    
    if start_block == end_block:
        # 같은 블록 안이면 직접 확인
        for i in range(a, b + 1):
            if A[i] < ans:
                ans = A[i]
    else:
        # 왼쪽 조각
        for i in range(a, (start_block + 1) * block_size):
            if A[i] < ans:
                ans = A[i]
        # 중간 블록들
        for idx in range(start_block + 1, end_block):
            if block_min[idx] < ans:
                ans = block_min[idx]
        # 오른쪽 조각
        for i in range(end_block * block_size, b + 1):
            if A[i] < ans:
                ans = A[i]
    
    result.append(str(ans))

print('\n'.join(result))