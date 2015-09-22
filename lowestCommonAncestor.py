"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        #Version 1 /does not work/this works for binary seach tree
        '''
        if root is None:
            return None
        if root.val > A.val and root.val > B.val:
            return self.lowestCommonAncestor(root.left, A, B)
        if root.val < A.val and root.val <B.val:
            return self.lowestCommonAncestor(root.right, A, B)
        return root
        '''
        #version 2 divide and conquer works
        # if root is None or root == A or root == B:
        #     return root
        # left = self.lowestCommonAncestor(root.left, A, B)
        # right = self.lowestCommonAncestor(root.right, A, B)
        
        # if left is not None and right is not None:
        #     return root
        # elif left is not None:
        #     return left
        # elif right is not None:
        #     return right
        # return None
        
        #version 3 not working this works for binary seach tree
        while root is not None:
            if root.val > A.val and root.val > B.val:
                root = root.left
            elif root.val < A.val and root.val < B.val:
                root = root.right
            else :
                break
        return root
        
        
