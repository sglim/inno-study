class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = []
        b = []

        for char in s:
            a.append(ord(char))

        for char in t:
            b.append(ord(char))

        a.sort()
        b.sort()
        if a == b:
            return True
        else:
            return False


s = 'bar'
t = 'rab'

obj = Solution()
print(obj.isAnagram(s, t))
