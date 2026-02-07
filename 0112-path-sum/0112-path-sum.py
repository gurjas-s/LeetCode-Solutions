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
 
            if not cur:
                continue
           
            curSum = sumQ.popleft() 
            if cur.left:
                leftCurSum = curSum + cur.left.val
                sumQ.append(leftCurSum)
                seen.add(leftCurSum)
            if cur.right:
                rightCurSum = curSum + cur.right.val
                sumQ.append(rightCurSum)            
                seen.add(rightCurSum)
            if not cur.left and not cur.right:
                if curSum == targetSum:
                    return True
            queue.append(cur.left)
            queue.append(cur.right)
  
        return False