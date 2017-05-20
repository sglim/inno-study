class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        result = 0
        s_len = len(s)
        t_len = len(t)
        length = 0
        longer = ''
        if s_len < t_len:
            length = s_len
            longer = t
        else:
            length = t_len
            longer = s

        for i in range(length):
            result ^= ord(s[i])
            result ^= ord(t[i])

        result ^= ord(longer[length])
        return chr(result)

s = ''
t = 'e'

obj = Solution()
print(obj.findTheDifference(s, t))
