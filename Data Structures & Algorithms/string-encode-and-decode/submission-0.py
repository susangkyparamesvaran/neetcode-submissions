class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for s in strs:
            encoded_string.append(str(len(s)))
            encoded_string.append("#")
            encoded_string.append(s)
        
        return "".join(encoded_string)


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_string = []
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length

            decoded_string.append(s[i:j])
            i = j

        return decoded_string