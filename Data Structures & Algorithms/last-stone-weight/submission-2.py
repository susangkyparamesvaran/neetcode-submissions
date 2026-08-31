class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0

        for stone in stones:
            max_heap.append(-stone)
        
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            if stone1 ==  stone2:
                continue
            else:
                remaining = abs(stone1 - stone2)
                heapq.heappush(max_heap, -remaining)
        
        if len(max_heap) == 0:
            return 0
        
        if len(max_heap) == 1:
            last_stone = heapq.heappop(max_heap)
            return (-last_stone)
