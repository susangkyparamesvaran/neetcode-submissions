class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        zero_count = 0
        total_product = 1

        for num in nums:
            if (num == 0):
                zero_count = zero_count + 1
            else:
                total_product = total_product * num
        
        for num in nums:
            if (zero_count > 1):
                value = 0
            elif (zero_count == 1):
                if (num == 0):
                    value = total_product
                else:
                    value = 0
            else:
                value = total_product / num
            


            solution.append(int(value))


        return solution  

        