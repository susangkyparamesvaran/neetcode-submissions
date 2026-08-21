class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        solution = []

        for i in range(len(s)):
            value = s[i]
            complement = 0 - value
            left = i + 1
            right = len(s) - 1

            while (left < right):
                sum = s[left] + s[right]
                if (sum == complement):
                    triplet = [s[i], s[left], s[right]]
                    if (triplet in solution):
                        left = left + 1
                    else:
                        solution.append(triplet)
                elif (sum < complement):
                    left = left + 1
                else:
                    right = right - 1

        return solution
            