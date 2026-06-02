# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def isIdentical(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None or p.val != q.val:
                return False

            return isIdentical(p.right, q.right) and isIdentical(p.left, q.left)
        
        
        
        identical_root = []

        stack = []
        stack.append(root)

        while len(stack) != 0:
            temp = stack.pop()
            if temp == None:
                continue
            if temp.val == subRoot.val:
                identical_root.append(temp)

            stack.append(temp.right)
            stack.append(temp.left)
        
        for nodes in identical_root:
            if isIdentical(nodes, subRoot):
                return True
        
        return False
        





