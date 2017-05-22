class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        hex_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

        if num == 0:
            return '0'

        elif num > 0:
            result = ''
            while num > 0:
                result = hex_char[num % 16] + result
                num //= 16
            return result

        # else:
        #     num *= -1
        #     count = 0
        #     result = ''
        #
        #     while num % 10 == 0:
        #         count += 1
        #         result += '0'
        #         num //= 10
        #
        #     for i in range(8 - count):
        #         digit = num % 10
        #         if i == 0:
        #             result = hex_char[16 - digit] + result
        #         else:
        #             result = hex_char[15 - digit] + result
        #         num //= 10
        #
        #     return result


num = -3949
obj = Solution()
print(obj.toHex(num))
