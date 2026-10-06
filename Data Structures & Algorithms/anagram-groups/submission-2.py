class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for word in strs:
            signature = "".join(sorted(word))

            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature] = [word]
            
        return list(groups.values())