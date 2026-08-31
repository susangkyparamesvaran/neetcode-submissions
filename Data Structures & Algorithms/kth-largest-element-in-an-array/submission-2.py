class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            max_heap.append(-num)
        
        heapq.heapify(max_heap)
        
        while k > 1:
            heapq.heappop(max_heap)
            k = k - 1

        return -max_heap[0]


        