# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        search_stack = []
        visit_hash = {}
        deepest_depth = -1

        if root is None:
            return 0

        search_stack.append((root, 1))

        while len(search_stack) > 0:
            node, depth = search_stack.pop()

            if node not in visit_hash:
                visit_hash[node] = True
                if depth > deepest_depth:
                    deepest_depth = depth
                if node.left is not None:
                    search_stack.append((node.left, depth + 1))
                if node.right is not None:
                    search_stack.append((node.right, depth + 1))

        return deepest_depth

