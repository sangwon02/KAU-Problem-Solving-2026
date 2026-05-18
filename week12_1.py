# 백준 11501
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    
    max_right = 0
    profit = 0
    
    
    for i in range(n - 1, -1, -1): # 미래에 값을 알고있는 것 부터 탐색
        if li[i] > max_right: # 원래 최대값보다 크면
            max_right = li[i] 
            
        else:
            profit += max_right - li[i] # 수익을 더함
            
    print(profit) 
        