class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        i = 5

        while n / i >= 1:
            result += (n // i)
            i *= 5

        return result


obj = Solution()
n = 99
result = obj.trailingZeroes(n)
print(result)
