# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        BFS traversal 
        When we visit a node we want to swap there left and right

        """
        queue = [root]
        seen = set()
    
        while queue:
            cur_node = queue.pop()

            if cur_node == None:
                continue 

            #swap

            temp = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = temp
           
            for node in [cur_node.right, cur_node.left]:
                queue.append(node)
     

        return root