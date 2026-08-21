class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a hash table with the frequency of characters of s1
        s1_freq = {}

        for char in s1:
            if char in s1_freq:
                s1_freq[char] = s1_freq.get(char, 0) + 1
            else:
                s1_freq[char] = 1
        
        # create a sliding window for s2, and create hash table for the substring
        # and compare the two hash tables

        s2_freq = {}
        start = 0

        for end in range(len(s2)):

            s2_freq[s2[end]] = s2_freq.get(s2[end],0) + 1

            while ((end-start+1) > len(s1)):
                s2_freq[s2[start]] -= 1

                if (s2_freq[s2[start]] == 0):
                    del s2_freq[s2[start]]

                start = start + 1

            if (s1_freq == s2_freq):
                return True

        return False


            
