class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_volume = 0

        while (left < right):
            num1 = heights[left]
            num2 = heights[right]

            calc_volume = (right - left) * min(num1, num2)

            if (calc_volume > max_volume):
                max_volume = calc_volume

            if (num1 < num2):
                left = left + 1
            else:
                right = right - 1
        
        return max_volume




