import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    st = input().rstrip()
    
    alnum_only = ''.join(filter(str.isalnum, st)) # 숫자와 알파벳만 가져오기
    alnum_only = alnum_only.upper() # 대문자로 변환
    stack = []
    
    for i in alnum_only:
        stack.append(i)
    for i in range(len(alnum_only)):
        if stack.pop() != alnum_only[i]:
            print("X")
            break
        
    else:
        print("O")
        