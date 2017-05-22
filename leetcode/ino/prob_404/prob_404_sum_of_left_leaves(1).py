# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                return root.left.val + self.sumOfLeftLeaves(root.right)

        result = 0
        result += self.sumOfLeftLeaves(root.left)
        result += self.sumOfLeftLeaves(root.right)

        return result


