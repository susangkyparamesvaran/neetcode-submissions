class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # pairs from hash table
        pairs = count.items()
        ordered = sorted(pairs, key = lambda item:item[1], reverse = True)

        solution = []
        i = 0
        while i < k:
            solution.append(ordered[i][0])
            i = i + 1
        
        return solution