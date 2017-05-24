class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        str_linked = s + s
        if s in str_linked[1:-1]:
            return True
        return False

s = 'abcabc'
obj = Solution()
print(obj.repeatedSubstringPattern(s))