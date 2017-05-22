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
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0 or carry:
            local_sum = 0
            if i >= 0:
                local_sum += self.char_to_int(num1[i])
                i -= 1
            if j >= 0:
                local_sum += self.char_to_int(num2[j])
                j -= 1
            local_sum += carry
            carry = local_sum // 10
            digit = local_sum % 10
            result = self.int_to_char(digit) + result

        return result


num1 = '99'
num2 = '1'
obj = Solution()
print(obj.addStrings(num1, num2))
