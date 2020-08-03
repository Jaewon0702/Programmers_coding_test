import heapq

def kth_smallest(nums,k) :
    heap=[]
    for num in nums :
        heapq.heappush(heap,num)

    kth_min=None
    for _ in range(k) :
        kth_min=heapq.heappop(heap)
    return kth_min

print(kth_smallest([4,1,7,3,8,5],3))
