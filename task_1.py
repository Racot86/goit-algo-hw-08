import heapq

def min_cost(cables):
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) > 1:
        
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        
        joint = a + b
        total_cost += joint

        heapq.heappush(cables, joint)
    return total_cost

cables = [2,8,6,4,1]
print(min_cost(cables))