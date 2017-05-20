class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        checker = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            checker[idx] += 1

        for char in t:
            idx = ord(char) - ord('a')
            checker[idx] -= 1

        result = 0
        if 1 in checker:
            result = checker.index(1)
        elif -1 in checker:
            result = checker.index(-1)

        return chr(result + ord('a'))

s = 'abcd'
t = 'abcde'

obj = Solution()
print(obj.findTheDifference(s, t))
