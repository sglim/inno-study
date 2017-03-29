class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result_dict = {}

        for i in range(len(nums)):
            if (nums[i] in result_dict) is True:
                return [result_dict[nums[i]], i]

            else:
                first_num = nums[i]
                result_dict[target - first_num] = i


test = Solution()
nums = [-3, -7, -8, -2]
target = -11


print(test.twoSum(nums,target))
