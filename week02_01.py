import sys
input = sys.stdin.readline

def solution(n):
    if n == 1:
        return "1"
    else:
        return solution(n-1) + " " + str(n) + " " + solution(n-1)

n = int(input())
print(solution(n))