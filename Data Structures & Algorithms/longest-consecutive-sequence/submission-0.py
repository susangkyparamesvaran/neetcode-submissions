class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a hash table that shows us what numbers we have
        seen = {}
        for num in nums:
            if num in seen:
                continue
            else:
                seen[num] = True

        if not seen:
            return 0

        # sort the keys of the hash table
        sorted_keys = sorted(seen.keys())

        i = 0
        longest = 1
        streak = 1
        for i in range(0, len(sorted_keys) - 1):
            value = sorted_keys[i] + 1

            if (sorted_keys[i+1] == value):
                streak = streak + 1
            else: 
                streak = 1
            
            if longest < streak:
                longest = streak
        
        return longest

