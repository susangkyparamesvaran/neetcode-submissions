class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        sum = 0

        def backtrack(i, total):

            if total == target:
                result.append(subset.copy())
                sum = 0
                return
            
            if i == len(nums) or total > target:
                return
            
            # skip the element
            backtrack(i + 1, total)

            # take the element
            subset.append(nums[i])
            backtrack(i, total + nums[i])

            # return the subset to original subset
            # before returning to parent
            subset.pop()
        
        backtrack(0, 0)
        return result
        