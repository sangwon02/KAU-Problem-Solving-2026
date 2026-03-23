import sys
input = sys.stdin.readline

x = int(input())
dp = [0] * (x + 1)
if x == 1:
    print(0)
    exit()

if x <= 3:
    print(1)
    exit()
    
dp[1] = 0
dp[2] = 1
dp[3] = 1

if x >= 4:
    for i in range(4, x + 1):
        dp[i] = dp[i - 1] + 1
        
        if i%2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
            
        if i%3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
            
print(dp[x])