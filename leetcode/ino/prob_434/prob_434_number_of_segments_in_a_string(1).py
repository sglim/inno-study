class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split(' '))


input_str = "Hello, my name is John"
obj = Solution()
print(obj.countSegments(input_str))
