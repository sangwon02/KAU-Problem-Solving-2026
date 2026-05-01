import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a_nums = list(map(int, input().split()))
    b_nums = list(map(int, input().split()))
    
    a_nums.sort()
    b_nums.sort()
    
    total_cnt = 0
    num_cnt = 0 # 현재 a_nums[a_pnt]보다 작은 b_nums의 개수
    
    a_pnt = 0
    b_pnt = 0
    
    while a_pnt < n and b_pnt < m:
        if a_nums[a_pnt] > b_nums[b_pnt]:
            num_cnt += 1
            b_pnt += 1
        else:
            total_cnt += num_cnt
            a_pnt += 1
            
    # b_num을 다 돈 경우
    while a_pnt < n:
        total_cnt += num_cnt
        a_pnt += 1
            
    print(total_cnt)