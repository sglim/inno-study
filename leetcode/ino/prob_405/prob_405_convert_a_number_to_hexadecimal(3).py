class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        hex_str = '0123456789abcdef'

        count = 8
        result = ''
        while num and count:
            result = hex_str[num & 15] + result
            num = num >> 4
            count -= 1

        return result

num = -3949
obj = Solution()
print(obj.toHex(num))
