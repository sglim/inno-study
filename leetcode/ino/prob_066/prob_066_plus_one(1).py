class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        input_num = 0
        result = []

        for num in digits:
            input_num *= 10
            input_num += num

        input_num += 1

        while input_num > 0:
            result.insert(0, input_num % 10)
            input_num //= 10

        return result


sol = Solution()
test = [9,9,9,9]

print(sol.plusOne(test))