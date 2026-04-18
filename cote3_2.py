import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li  = list(map(int, input().split()))  # 일단 옷들을 리스트에 저장
set = set(li) # 집합을 통해 중복된거 제거

if N == len(li) == len(set): # 사람의 수와 옷의 개수와 옷의 종류수가 같으면
    print("Yes")
else:
    print("No")
    
if M == len(set):
    print("Yes")
else:
    print("No")