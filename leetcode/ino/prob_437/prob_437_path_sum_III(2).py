# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def helper(self, node, target, before_sum, dict):
        if node is None:
            return

        complement = before_sum + node.val - target
        if complement in dict:
            self.result += dict[complement]
        dict.setdefault(before_sum + node.val, 0)
        dict[before_sum + node.val] += 1
        self.helper(node.left, target, before_sum + node.val, dict)
        self.helper(node.right, target, before_sum + node.val, dict)
        dict[before_sum + node.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0: 1})
        return self.result





