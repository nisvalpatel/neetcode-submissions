from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #to implement binary tree level traversal, i will have to use a queue where
        #it is first in and first out

        if root == None:
            return []

        ret_list = []
        q = deque()
        q.append(root)

        while len(q) != 0:
            temp_list = []
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                temp_list.append(curr.val)
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)

            ret_list.append(temp_list)
            
        return ret_list


        


        