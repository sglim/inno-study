class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        s = s[::-1]

        for power in range(len(s)):
            char = s[power]
            num = ord(char) - ord('A') + 1
            result += ((26**power) * num)

        return result

obj = Solution()
s = 'BA'
print(obj.titleToNumber(s))
