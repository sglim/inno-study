class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.length = len(nums)
        if self.length > 0:
            self.sum_arr = [0] * self.length
            self.sum_arr[0] = nums[0]
            for i in range(1, self.length):
                self.sum_arr[i] = nums[i] + self.sum_arr[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j or self.length == 0:
            return None
        if i == 0:
            return self.sum_arr[j]

        return self.sum_arr[j] - self.sum_arr[i-1]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)
print(obj.sumRange(0, 2)) # 1
print(obj.sumRange(2, 5)) # -1
print(obj.sumRange(0, 5)) # -3
