class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1

        while (start <= end):
            midpoint = (start + end) // 2

            if (target == nums[midpoint]):
                return midpoint
            elif (target < nums[midpoint]):
                end = midpoint - 1
            else:
                start = midpoint + 1
        
        return -1

