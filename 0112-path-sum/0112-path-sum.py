# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque
        if not root:
            return False
        queue = deque()
        queue.append(root)
        
        sumQ = deque()
        sumQ.append(root.val) 
        seen = set()
 
        while queue: 
            cur=queue.popleft()  
            # if not cur: #ignore null
            #     continue
           
            curSum = sumQ.popleft() 
            if cur.left: #visit neighbour step
                leftCurSum = curSum + cur.left.val
                sumQ.append(leftCurSum)
                queue.append(cur.left) 
            if cur.right:#visit neighbour
                rightCurSum = curSum + cur.right.val
                sumQ.append(rightCurSum)            
                queue.append(cur.right)
            if not cur.left and not cur.right: #if leaf node check if sum in thisd path equals target
                if curSum == targetSum:
                    return True
            

  
        return False