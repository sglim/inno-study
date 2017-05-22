class Solution(object):
    def char_to_int(self, c):
        return ord(c) - ord('0')

    def int_to_char(self, i):
        return chr(i + ord('0'))

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        result = ''

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        num1 = num1[::-1]
        num2 = num2[::-1]

        num1 = num1 + '0'
        for i in range(len(num2)):
            a = self.char_to_int(num1[i])
            b = self.char_to_int(num2[i])
            local_sum = carry + a + b
            carry = local_sum // 10
            result = self.int_to_char(local_sum % 10) + result

        last_digit = len(num2)
        for i in range(last_digit, len(num1)):
            a = self.char_to_int(num1[i])
            local_sum = carry + a
            carry = local_sum // 10
            result = self.int_to_char(local_sum % 10) + result

        if result[0] == '0':
            return result[1:]
        else:
            return result


num1 = '0'
num2 = '0'
obj = Solution()
print(obj.addStrings(num1, num2))
