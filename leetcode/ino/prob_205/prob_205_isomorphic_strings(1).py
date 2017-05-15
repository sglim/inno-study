class Solution(object):
    def string_check(self, s):
        n = len(s)
        arr = []

        num_now = 1
        check_hash = {}
        for char in s:
            if char in check_hash:
                arr.append(check_hash[char])
            else:
                arr.append(num_now)
                check_hash[char] = num_now
                num_now += 1
        return arr

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        checker_s = self.string_check(s)
        checker_t = self.string_check(t)

        if checker_s == checker_t:
            return True
        else:
            return False


obj = Solution()
s = 'paper'
t = 'title'

print(obj.isIsomorphic(s, t))
