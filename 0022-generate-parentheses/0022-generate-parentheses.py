class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(stack, cur, res): 
            
                
 
                 
            if len(cur)==(2*n): #to do add if valid sequence before appending
                if len(stack) == 0:
                    res.append(cur) 
                return 
            
            next1, next2 = cur, cur
            next1 += '('
            next2 += ')'
            stack1 = stack.copy()
            stack.append('(')
            #update stacks
            dfs(stack, next1, res)                

            if stack1:
                stack1.pop()
                dfs(stack1, next2, res)
            
            return res #final output array

        res = []
        stack = ['(']
        output = dfs(stack, '(', res)
        print(output)
        return output

    