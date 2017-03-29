class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = [0, 0]

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result[0] = i
                    result[1] = j
                    break

        return result

sol = Solution()

nums = [2, 7, 11, 15]
target = 9

print(sol.twoSum(nums, target))

