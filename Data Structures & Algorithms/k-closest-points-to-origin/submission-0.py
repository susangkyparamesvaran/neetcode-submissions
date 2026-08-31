class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # once again lets keep the size of the heap as k
        # we need min heap for the closest points
        min_heap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x**2 + y**2
            min_heap.append([distance, point])
            
        heapq.heapify(min_heap)

        res = []
        while k > 0:
            dist, point = heapq.heappop(min_heap)
            res.append(point)
            k = k - 1
        
        return res