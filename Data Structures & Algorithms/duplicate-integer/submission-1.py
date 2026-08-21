class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create an empty hash table
        seen = {}
        # check each value in list
        for num in nums:
            # if it is in seen, return True
            if num in seen:
                return True
            
            seen[num] = True
        
        return False