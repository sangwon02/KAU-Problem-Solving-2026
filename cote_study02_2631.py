import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))
sumli = [0]

sumnum = 0

for i in li:
    sumnum += i
    sumli.append(sumnum)

left = 0
right = 1
cnt = 0

while right <= n: # 오른쪽 포인터가 끝까지 가면 종료
    # 현재 탐색중인 합
    current_sum = sumli[right] - sumli[left]
    
    # 만약 조건에 맞으면
    if current_sum == k:
        cnt += 1 # 카운트 1 올려주고
        left += 1 # 왼쪽에 있는 포인터 이동
        
    elif current_sum < k: # 합이 더 작으면
        right += 1 # 오른쪽에 있는걸 이동
    else: # 합이 더 크면
        left += 1 # 왼쪽에 있는 포인터를 이동
        
    if left == right and right <= n: # 왼쪽 포인터가 오른쪽 포인터를 벗어나면 안됨!
        right += 1

print(cnt)

    
