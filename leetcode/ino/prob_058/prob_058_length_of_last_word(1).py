class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

    def plus_one(digits):
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            s = num + 1 + carry
            carry = s // 10
            s %= 10
            digits[i] = s

        if carry:
            digits.insert(0, carry)

        return carry


sol = Solution()
test_str = "a "

print(sol.lengthOfLastWord(test_str))
