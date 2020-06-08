import heapq as heap

l = []
heap.heappush(l, 20)
heap.heappush(l, 14)
heap.heappush(l, 5)
heap.heappush(l, 15)
heap.heappush(l, 10)
heap.heappush(l, 2)

print(l)
print(heap.heappop(l))
print(l)
heap.heappushpop(l,18)
print(l)
 
l1 = heap.nlargest(3,l)
print(l1)
l2 = heap.nsmallest(3, l)
print(l2)

l3 = [20,14,2,15,10,21]
print(l3)
heap.heapify(l3)
print(l3)