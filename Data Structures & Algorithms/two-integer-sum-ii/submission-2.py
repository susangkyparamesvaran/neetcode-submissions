class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1

        while (index1< index2):
            value = numbers[index1] + numbers[index2]
            if (value == target):
                return [index1 + 1, index2 + 1]
            elif (value < target):
                index1 = index1 + 1
            else:
                index2 = index2 - 1
        