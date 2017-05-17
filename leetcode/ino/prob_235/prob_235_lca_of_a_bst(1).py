# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None

        self.a = None
        self.b = None
        self.result = None
        if p.val <= q.val:
            self.a, self.b = p, q
        else:
            self.a, self.b = q, p

        if self.b.val < root.val:
            self.result = self.lowestCommonAncestor(root.left, p, q)
        elif root.val < self.a.val:
            self.result = self.lowestCommonAncestor(root.right, p, q)
        else:
            self.result = root

        return self.result


test_arr = [6,2,8,0,4,7,9]
root = None
cur = None
queue = []
for i in range(0, len(test_arr), 2):
    if i == 0:
        root = TreeNode(test_arr[i])
        queue.append(root)
    else:
        cur = queue.pop(0)
        cur.left = TreeNode(test_arr[i-1])
        cur.right = TreeNode(test_arr[i])
        queue.append(cur.left)
        queue.append(cur.right)


p = TreeNode(3)
q = TreeNode(5)

obj = Solution()
result = obj.lowestCommonAncestor(root, p, q)
if result is None:
    print(result)
else:
    print(result.val)
