class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()

        start = 0
        end = 0

        if len(s) == 1:
            return 1
        
        # this is for strings longer than 2
        while (end < len(s)):
            while ((s[end]) in seen):
                seen.remove(s[start])
                # restart dictionaries and move window
                start = start + 1
            substring = s[start:end]
            longest = max(longest, len(substring) + 1)
            seen.add(s[end])
            end = end + 1

        return longest
