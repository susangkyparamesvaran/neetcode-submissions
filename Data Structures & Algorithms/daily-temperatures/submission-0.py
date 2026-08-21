class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temp = []
        result = [0] * len(temperatures)

        for index in range(0, len(temperatures)):
            value = temperatures[index]
            while ((len(temp)) and (value > temp[-1][0])):
                # if it is bigger, then calculate the difference between the indexes
                key = temp[-1][1]
                result[key] = index - key
                # and pop the values
                temp.pop()
            
            temp.append((value,index))
        
        return result

            
                    

                
