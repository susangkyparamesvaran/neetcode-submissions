class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create a hash table to track frequency of a number in array
        count = {}
        solution = []

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        freq = sorted(count.items(), key = lambda item: item[1], reverse = True)

        for i in range(k):
            solution.append(freq[i][0])
        
        return solution
        