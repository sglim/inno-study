# time limit fail
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        if len(nums) < 3:
            return result

        for start in range(0, len(nums)):
            if (nums[start] != nums[start - 1] and start > 0) or start == 0:
                mid, end = start + 1, len(nums) - 1
                while mid < end:
                    if nums[start] + nums[mid] + nums[end] == 0:
                        result.append([nums[start], nums[mid], nums[end]])
                        while mid < end and nums[mid] == nums[mid + 1]:
                            mid += 1
                        while mid < end and nums[end] == nums[end - 1]:
                            end -= 1

                    if nums[start] + nums[mid] + nums[end] < 0:
                        mid += 1
                    else:
                        end -= 1

        return result


# nums = [-1,0,1,2,-1,-4]
# nums = [0, 0, 0, 0]
nums = [-2,0,1,1,2]
obj = Solution()
print(obj.threeSum(nums))

