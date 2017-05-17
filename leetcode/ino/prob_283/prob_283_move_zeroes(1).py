class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        checker = -1
        for cur in range(len(nums)):
            if checker < 0 and nums[cur] == 0:
                checker = cur
            if checker >= 0 and nums[cur] != 0:
                nums[checker], nums[cur] = nums[cur], nums[checker]
                checker += 1


test_arr = [1, 3, 12]
obj = Solution()
obj.moveZeroes(test_arr)
print(test_arr)
