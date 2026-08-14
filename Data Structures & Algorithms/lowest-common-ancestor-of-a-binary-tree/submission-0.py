# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def dfs(curr):
            if curr == None or curr == p or curr == q:
                return curr

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left and right:
                return curr
            
            if left != None:
                return left
            
            if right != None:
                return right
            
            
            return None
        
        return dfs(root)
