class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {'+','-','*','/'}
        stack = []

        for token in tokens:
            if token not in operator:
                stack.append(token)
            else:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                
                if (token == '+'):
                    value = operand1 + operand2
                elif (token == '-'):
                    value = operand1 - operand2
                elif (token == '*'):
                    value = operand1 * operand2
                else:
                    value = operand1 / operand2
                
                stack.append(value)
        
        return int(stack.pop())
