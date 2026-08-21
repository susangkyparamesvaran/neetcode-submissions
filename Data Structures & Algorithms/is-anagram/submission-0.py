class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # to prove that words are anagrams we jus need to show that 
        # each letter has the same frequency

        # split strings into arrays so we can loop through them
        s_array = list(s)
        t_array = list(t)

        # create a hash table to record frequency of s and t
        s_freq = {}
        for char in s_array:
            s_freq[char] = s_freq.get(char, 0) + 1

        t_freq = {}
        for char in t_array:
            t_freq[char] = t_freq.get(char, 0) + 1
        
        if (s_freq == t_freq):
            return True

        return False

        