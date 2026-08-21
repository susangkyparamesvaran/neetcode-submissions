class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        # for each word create a signature
        for word in strs:
            signature = "".join(sorted(word))
            if signature not in groups:
                groups[signature] = []
                groups[signature].append(word)
            else:
                groups[signature].append(word)
                
        return list(groups.values())