# 백준 1202번 보석 도둑
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))
jewels.sort()  # 보석을 무게 기준으로 오름차순 정렬

bags = []
for _ in range(k):
    c = int(input())
    bags.append(c)
bags.sort()  # 무게 기준으로 정렬

heap = []
result = 0
check = 0
for bag in bags:
    while check < n and jewels[check][0] <= bag: # 보석의 무게가 가방의 용량보다 작거나 같으면
        heapq.heappush(heap, -jewels[check][1])  # 보석의 가치를 힙에 추가
        check += 1
    
    if heap:
        result -= heapq.heappop(heap) # 가장 가치가 높은 보석을 가방에 넣음
        
print(result)