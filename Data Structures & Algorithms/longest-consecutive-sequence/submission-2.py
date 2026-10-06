class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check what values are in the list
        seen = {}

        for num in nums:
            if num in seen:
                continue
            else:
                seen[num] = True
        
        if not seen:
            return 0

        order = sorted(seen.keys())

        i = 0
        longest = 1
        streak = 1

        for i in range(0, len(order) - 1):
            value = order[i] + 1
            if (order[i+1] == value):
                streak = streak + 1
            else:
                streak = 1
            
            if longest < streak:
                longest = streak
        
        return longest

             