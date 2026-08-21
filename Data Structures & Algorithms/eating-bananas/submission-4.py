class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        start = 1
        end = max(piles)

        while (start <= end):
            rate = (start + end) // 2
            hours = 0

            for i in range(len(piles)):
                hours = hours + math.ceil(piles[i] / rate)
                
            if (hours <= h):
                end = rate - 1
            else:
                start = rate + 1
            
        return start