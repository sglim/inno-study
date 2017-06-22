# time limit...

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x == 0:
            return 0

        left = 1
        right = x

        # invariant : answer should be placed in [left, right)
        while left <= right:
            mid = left + (right - left) // 2
            mid_sq = mid * mid

            if mid_sq <= x:
                left = mid + 1
            else:
                right = mid - 1
        # at this time, left == right
        return left

obj = Solution()
x = 15
print(obj.mySqrt(x))


