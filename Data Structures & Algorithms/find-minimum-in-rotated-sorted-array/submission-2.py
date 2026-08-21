class Solution:
    def findMin(self, nums: List[int]) -> int:

        # we could iterate until we found a value that decreased rather than increasing
        # but this would be O(n), because the worst case is its only ahd a rotation of 
        # 1 so you've searched every value

        # we can reduce the search values, by using the midpoint to find out which the  side of the list the minimum is

        start = 0
        end = len(nums) - 1

        while (start < end):
            midpoint = (start + end) // 2
            
            if (nums[midpoint] > nums[end]):
                start = midpoint + 1
            else:
                # nums[midpoint] < nums[end]
                end = midpoint
            
        return nums[start]

        

        
        