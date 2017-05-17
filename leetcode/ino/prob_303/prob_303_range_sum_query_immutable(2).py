'''
applying fenwick tree
'''

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.update(i, nums[i-1])

    def update(self, i, num):
        while i <= self.n:
            self.tree[i] += num
            i += (i & -i)

    def tree_sum(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= (i & -i)

        return ans

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.tree_sum(j+1) - self.tree_sum(i)


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)
print(obj.sumRange(0, 2)) # 1
print(obj.sumRange(2, 5)) # -1
print(obj.sumRange(0, 5)) # -3
