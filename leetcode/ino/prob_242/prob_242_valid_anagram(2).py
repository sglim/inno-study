class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        check_hash = {}

        for char in s:
            if char in check_hash:
                check_hash[char] += 1
            else:
                check_hash[char] = 1

        for char in t:
            if char in check_hash:
                check_hash[char] -= 1
                if check_hash[char] < 0:
                    return False
            else:
                return False

        return True


s = 'bar'
t = 'raba'

obj = Solution()
print(obj.isAnagram(s, t))
