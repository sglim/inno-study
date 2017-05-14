class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = ''
        alpha = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']

        while n != 0:
            rest = n % 26
            result = alpha[rest] + result
            n = n // 26
            if rest == 0:
                n -= 1

        return result


obj = Solution()
n = 26*3 - 1

print(obj.convertToTitle(n))