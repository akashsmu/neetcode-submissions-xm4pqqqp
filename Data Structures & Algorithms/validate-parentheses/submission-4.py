class Solution:
    def isValid(self, s: str) -> bool:
        valid = { ')' : '(' , ']' : '[', '}' : '{'}
        stack = []
        for par in s:
            if par in valid:
                if stack and stack[-1] == valid[par]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(par)

        return True if not stack else False
            
