"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        #version 1 not working
        #http://www.jiuzhang.com/solutions/binary-tree-level-order-traversal/
        result = []
        if root is None:
             return result
        q = Queue.Queue(0)
        q.put(root)
        while not q.empty(): 
            #it is q.empty() not q.empty
            level = []
            size = q.qsize()
            for i in range(size):
                head = q.get()
                level.append(head.val)
                if head.left is not None:
                    q.put(head.left)
                if head.right is not None:
                    q.put(head.right)
            result.append(level)
        return result
        #version 2
    '''
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result
        '''
def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().levelOrder(root)
    print result
if __name__ == '__main__':
    main()
        