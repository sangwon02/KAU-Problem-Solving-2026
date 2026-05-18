# 백준 7662
import sys
import heapq
input = sys.stdin.readline  

tc = int(input())

for _ in range(tc):
    n = int(input())  
    
    # i번째 연산으로 삽입된 원소가 삭제됐는지 표시
    isDeleted = [False] * n
    
    minHeap = []  # (값, 연산번호) top이 최솟값
    maxHeap = []   # (-값, 연산번호) top이 최댓값 
    
    for i in range(n):
        cmd, target = input().rstrip().split()
        target = int(target)
        # 삽입 연산
        if cmd == 'I':
            heapq.heappush(minHeap, (target, i))
            heapq.heappush(maxHeap, (-target, i))   
        # 삭제 연산
        else:
            if target == 1:  
                while maxHeap and isDeleted[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                
                if maxHeap:
                    _, key = heapq.heappop(maxHeap)
                    isDeleted[key] = True  
            
            else:  
                while minHeap and isDeleted[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                
                if minHeap:
                    _, key = heapq.heappop(minHeap)
                    isDeleted[key] = True
                    
                    
    while maxHeap and isDeleted[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    while minHeap and isDeleted[minHeap[0][1]]:
        heapq.heappop(minHeap)

    if not minHeap:
        print("EMPTY")
    else:
        print(-maxHeap[0][0], minHeap[0][0])