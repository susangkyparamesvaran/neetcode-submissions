class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        
        def backtrack(i, path):
            if i == len(nums):
                result.append(path.copy())
                return

            # DON'T take nums[i]
            backtrack(i + 1, path)

            # TAKE nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

        backtrack(0, [])

        return result
        