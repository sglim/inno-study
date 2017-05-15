class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = ''

        while n != 0:
            n -= 1
            result = chr(n % 26 + ord('A')) + result
            n = n // 26

        return result


obj = Solution()
n = 26

print(obj.convertToTitle(n))