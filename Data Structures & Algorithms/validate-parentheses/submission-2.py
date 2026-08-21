class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {}

        parentheses['}'] = '{'
        parentheses[')'] = '('
        parentheses[']'] = '['

        stack = []
    
        for par in s:
            if par not in parentheses:
                stack.append(par)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (top != parentheses[par]):
                    return False
        
        return (len(stack) == 0)
        
