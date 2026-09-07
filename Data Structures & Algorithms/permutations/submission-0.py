class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        used = {}

        def backtrack():
            
            # base case
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return

            # so we choose a number:
                # if the number is in used then we skip it
                # otherwise we add then remove the elements, the same we did with subsets
            
            for num in nums:
                if num in used:
                    continue
                
                # take value
                permutation.append(num)
                used[num] = True
                
                backtrack()

                # return to original state
                permutation.pop()
                del used[num]

        backtrack()
        return result