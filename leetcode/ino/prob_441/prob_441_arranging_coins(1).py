class Solution(object):
    def cal_s(self, i):
        return i * (i + 1) // 2

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        start = 1
        end = int((2*n)**0.5) + 1

        while start < end:
            mid = start + (end - start) // 2 + 1
            s = self.cal_s(mid)

            if s > n:
                end = mid - 1
            else:
                start = mid

        return start


n = 0
obj = Solution()
print(obj.arrangeCoins(n))