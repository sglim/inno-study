class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()

        g_ptr = 0
        s_ptr = 0

        count = 0

        while g_ptr < len(g) and s_ptr < len(s):
            if g[g_ptr] <= s[s_ptr]:
                count += 1
                g_ptr += 1
                s_ptr += 1
            else:
                s_ptr += 1

        return count


g = [1, 2]
s = [1, 2, 3]

obj = Solution()
print(obj.findContentChildren(g, s))
