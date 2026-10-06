class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] = target - nums[j]
        difference = {}
        for i in range(0,len(nums)):
            value = target - nums[i]
            if value in difference:
                return [difference[value], i]

            difference[nums[i]] = i