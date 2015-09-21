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
    @return: True if this Binary tree is Balanced, or false.
    """
    # my version
  
    def isBalanced(self, root):
        # write your code here
        if root == None:
            return True
        stack = [root]
        while stack:
            root = stack.pop()
            if self.depth(root) > 0:
                if abs(self.depth(root.left) - self.depth(root.right)) > 1:
                    return False
                stack.append(root.left)
                stack.append(root.right)
        return True
        
    def depth(self,root):
        if root == None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
    
    '''
    #Jiuzhang's version
    def isBalanced(self,root):
        isBalanced, _ = self.validate(root)
        return isBalanced
    def validate(self,root):
        if root == None:
            return True, 0 
        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False,0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False,0
        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1
        '''