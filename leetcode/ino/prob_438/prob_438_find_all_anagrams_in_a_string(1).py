# time limit fail

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s = len(s)
        len_p = len(p)
        if len_s < len_p:
            return []

        result = []
        p = list(p)
        p.sort()

        for i in range(len_s - len_p + 1):
            temp = list(s[i:i+len_p])
            temp.sort()

            if temp == p:
                result.append(i)

        return result


s = "abab"
p = "ab"
obj = Solution()
print(obj.findAnagrams(s, p))
#
#
# a = list('abc')
# b = list('cba')
# a.sort()
# b.sort()
# print(a)
# print(b)
#
# print(a == b)
