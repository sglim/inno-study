class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            if n & 1:
                result += 1
            n = n >> 1

        return result


obj = Solution()
n = 11

print(obj.hammingWeight(n))