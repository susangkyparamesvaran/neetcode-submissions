class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        left = 0
        right = len(s) -1

        while (left < right):
            left_al = string[left].isalnum()
            right_al = string[right].isalnum()

            if (left_al == False):
                left = left + 1
            elif (right_al == False):
                right = right - 1
            elif (string[left] == string[right]):
                left = left + 1
                right = right - 1
            else:
                return False
        
        return True
            

        