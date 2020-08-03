import heapq
nums=[4,1,7,3,8,5]
heap=[]

for num in nums :
    heapq.heappush(heap,(-num,num))

while heap :
    print(heapq.heappop(heap)[1])
