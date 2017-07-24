# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # Recursive Solution
        if root == None:    # Base condition
            return True
        else:
            return self.isSym(root.left, root.right)
        
    def isSym(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        
        if left.val == right.val:
            outer = self.isSym(left.left, right.right)
            inner = self.isSym(left.right, right.left)
            return outer and inner
        else:
            return False