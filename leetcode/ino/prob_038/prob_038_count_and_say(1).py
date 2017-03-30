class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = '1'

        if n == 1:
            return result

        while n - 1 > 0:
            result = self.get_next(result)
            n -= 1

        return result

    def get_next(self, input_str):
        current = input_str[0]
        count = 1
        next_str = ''

        for ch in input_str[1:]:
            if ch == current:
                count += 1
            else:
                next_str = next_str + str(count) + current
                current = ch
                count = 1

        return next_str + str(count) + current


sol = Solution()
n = 5

print(sol.countAndSay(n))