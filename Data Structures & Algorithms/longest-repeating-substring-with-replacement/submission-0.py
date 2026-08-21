class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        max_freq = 0
        seen = {}
        start = 0
        for end in range(len(s)):
            seen[s[end]] = seen.get(s[end], 0) + 1
            
            max_freq = max(max_freq, seen[s[end]])

            while ((end - start + 1) - max_freq) > k:
                seen[s[start]] = seen.get(s[start],0) - 1
                start = start + 1
            
            longest = max(longest, end-start + 1)
        
        return longest


