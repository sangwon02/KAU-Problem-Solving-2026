import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

cnt = [0] * n
nearest = [-1] * n 

stack = []
for i in range(n):
    while stack and li[stack[-1]] <= li[i]:
        stack.pop()
    
    cnt[i] += len(stack)
    if stack:
        nearest[i] = stack[-1]
    stack.append(i)

stack = []
for i in range(n - 1, -1, -1):
    while stack and li[stack[-1]] <= li[i]:
        stack.pop()
    
    cnt[i] += len(stack)
    if stack:
        right_idx = stack[-1]
        if nearest[i] == -1:
            nearest[i] = right_idx
        else:
            if abs(i - right_idx) < abs(i - nearest[i]):
                nearest[i] = right_idx
    stack.append(i)

ans = []
for i in range(n):
    if cnt[i] > 0:
        ans.append(f"{cnt[i]} {nearest[i] + 1}")
    else:
        ans.append("0")

print("\n".join(ans))