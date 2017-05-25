class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = ''
        while num > 0:
            if num & 1:
                result = '0' + result
            else:
                result = '1' + result
            num = num >> 1

        result = '0b' + result
        return int(result, 2)

num = 5
obj = Solution()
print(obj.findComplement(num))
