# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sum_check(self, node, target):
        if node is None:
            return 0

        num_of_paths = 0
        next_target = target - node.val
        if next_target == 0:
            num_of_paths += 1

        num_of_paths += self.sum_check(node.left, next_target)
        num_of_paths += self.sum_check(node.right, next_target)

        return num_of_paths

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        paths = 0
        if root is None:
            return paths

        node_queue = []
        node_queue.append(root)

        while len(node_queue) != 0:
            cur_node = node_queue.pop()
            if cur_node.left:
                node_queue.append(cur_node.left)
            if cur_node.right:
                node_queue.append(cur_node.right)
            paths += self.sum_check(cur_node, sum)

        return paths




