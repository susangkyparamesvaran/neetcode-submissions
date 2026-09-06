class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(i, path):
            if i == len(nums):
                result.append(path.copy())
                return
            
            # add current index
            path.append(nums[i])
            backtrack(i + 1, path)

            # path is a shared list
            # so return to its original 
            # state before returning to the parent
            path.pop()

            # skip the current index
            backtrack(i + 1, path)


        backtrack(0, [])

        return result
        