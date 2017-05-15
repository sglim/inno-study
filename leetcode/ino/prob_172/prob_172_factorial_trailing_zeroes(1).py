# fail...

import math

class Solution(object):
    def check_zeros(self, left, right, limit):
        if left == right:
            value = left
            zeros = 0

            return value, zeros

        mid = (left + right) // 2
        left_value, left_zeros = self.check_zeros(left, mid, limit)
        right_value, right_zeros = self.check_zeros(mid + 1, right, limit)

        value = left_value * right_value
        if value > limit:
            value %= limit
        zeros = left_zeros + right_zeros

        while value % 10 == 0:
            zeros += 1
            value /= 10

        return value, zeros


    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        limit = 10 ** (math.ceil(math.log10(n)) * 2)
        value, zeros = self.check_zeros(1, n, limit)
        return zeros


obj = Solution()
n = 6324
result = obj.trailingZeroes(n)
print(result)
