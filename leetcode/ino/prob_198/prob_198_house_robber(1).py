class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        d = [[0] * 2 for i in range(n)]
        d[0][1] = nums[0]

        for i in range(1, n):
            d[i][0] = max(d[i-1][0], d[i-1][1])
            d[i][1] = d[i-1][0] + nums[i]

        return max(d[n-1][0], d[n-1][1])


test_arr = [1, 0, 7, 3, 5]
obj = Solution()
print(obj.rob(test_arr))
