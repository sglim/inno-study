class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num

        result = num % 9
        if result == 0:
            return 9
        else:
            return result


num = 23
obj = Solution()
print(obj.addDigits(num))
