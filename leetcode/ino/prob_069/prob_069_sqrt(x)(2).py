# time limit...

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x <= 1:
            return x

        left = 1
        right = x - 1

        # invariant : answer should be placed in [left, right]
        while left <= right:
            mid = left + (right - left) // 2
            mid_sq = mid * mid

            if mid_sq < x:  # desired index should be larger than mid
                left = mid + 1
            elif mid_sq > x:  # desired index should be smaller than mid
                right = mid - 1
            else:
                return mid
        # at this time, left > right
        return right

obj = Solution()
x = 0
print(obj.mySqrt(x))


