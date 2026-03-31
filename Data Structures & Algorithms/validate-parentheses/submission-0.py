class Solution:
    def isValid(self, s: str) -> bool:

        curves = {']':'[', '}':'{', ')':'('}
        closing = set(']})')
        stack = []

        for curl in s:

            if curl in curves and stack :
                if curves[curl] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(curl)
        
        return False if stack else True
            

