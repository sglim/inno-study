class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)

sol = Solution()
test_arr = [1,3,5,6]
test_target = 0

print(sol.searchInsert(test_arr,test_target))