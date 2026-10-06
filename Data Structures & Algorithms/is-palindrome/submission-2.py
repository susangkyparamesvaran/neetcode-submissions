class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()

        left = 0
        right = len(string) -1

        while (left < right):
            if (string[left].isalnum() == False):
                left = left + 1
            elif (string[right].isalnum() == False):
                right = right - 1
            elif (string[left] == string[right]):
                left = left + 1
                right = right - 1
            else:
                return False
        
        return True

