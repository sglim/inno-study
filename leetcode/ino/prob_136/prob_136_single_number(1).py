class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for num in nums:
            result ^= num

        return result

# testing

sol = Solution()
test_input = [2,1,4,5,2,4,1]
print(sol.singleNumber(test_input))
