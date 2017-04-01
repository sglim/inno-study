# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        elif p is not None and q is not None:
            left = self.isSameTree(p.left, q.left)
            if left is False:
                return False
            if p.val != q.val:
                return False
            right = self.isSameTree(p.right, q.right)
            if right is False:
                return False
            return True

        else:
            return False

