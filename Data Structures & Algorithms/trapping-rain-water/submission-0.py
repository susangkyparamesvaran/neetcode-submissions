class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        # left max at each index
        for i in range(1, len(height)):
            left = max(left_max[i-1], height[i-1])
            left_max[i] = left
        

        # right max at each index
        for i in range(len(height)-2, 0, -1):
            right = max(right_max[i+1], height[i+1])
            right_max[i] = right

        for i in range(0, len(height)):
            max_water = min(left_max[i], right_max[i])
            water = max_water - height[i]

            if (water > 0):
                total = total + water
        
        return total







