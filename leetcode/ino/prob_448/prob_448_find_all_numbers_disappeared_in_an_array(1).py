class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result

test_input = [4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDisappearedNumbers(test_input))
