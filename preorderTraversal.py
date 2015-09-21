"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        #version 1 Traverse:
        # if root is None:
        #     return []
        # stack = [root]
        # preorder = []
        # while stack:
        #     node = stack.pop()
        #     preorder.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return preorder
        
        #version 2 divide and conquer
            result = []
            if root == None:
                return result
            #divide
            left = self.preorderTraversal(root.left)
            right = self.preorderTraversal(root.right)
            #conquer
            result.append(root.val)
            result = result +left
            result = result + right
            return result
            
