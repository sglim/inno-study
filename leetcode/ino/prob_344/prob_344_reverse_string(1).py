class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        return s[::-1]

test_str = 'abcdefg'
obj = Solution()
print(obj.reverseString(test_str))
