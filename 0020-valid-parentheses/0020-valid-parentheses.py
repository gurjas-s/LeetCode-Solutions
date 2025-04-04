class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {'(':')', '{':'}', '[':']'}
        stack = [] 

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                #if no open brackets or open bracket doesn't match return false
                if len(stack) == 0 or brackets[stack[-1]]!=bracket:
                    return False
                stack.pop() #remove open bracket
        print(stack)
        return len(stack) == 0 #if all open brackets have been matched return true