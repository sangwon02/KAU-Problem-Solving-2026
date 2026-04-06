import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split(",")))

for _ in range(k):
    li = [li[i+1] - li[i] for i in range(len(li)-1)]

for i in range(len(li)-1):
    print(li[i], end =",")
    
print(li[-1])