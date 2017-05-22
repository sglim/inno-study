class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        hex_char = '0123456789abcdef'
        result = ''.join(hex_char[(num >> (4 * i)) & 15] for i in range(8))
        result = result[::-1]

        if not result.lstrip('0'):
            return '0'
        else:
            return result.lstrip('0')


num = 26
obj = Solution()
print(obj.toHex(num))

