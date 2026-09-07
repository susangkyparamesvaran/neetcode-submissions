class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        nums.sort()

        def backtrack(i, subset):
            # base case
            if i == len(nums):
                result.append(subset.copy())
                return
            
            # take value
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # return to parent
            subset.pop()

            # skip value
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i = i + 1
            
            backtrack(i + 1, subset)

        backtrack(0, [])
        return result