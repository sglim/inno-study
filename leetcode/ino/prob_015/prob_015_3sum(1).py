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
            if nums[start] == nums[start - 1] and start != 0:
                continue

            mid, end = start + 1, len(nums) - 1
            while mid < end:
                if nums[mid] == nums[mid - 1] and mid != start + 1:
                    mid += 1
                    continue

                a, b, c = nums[start], nums[mid], nums[end]
                cur_comb = [a, b, c]
                cur_sum = sum(cur_comb)

                if cur_sum == 0:
                    result.append(cur_comb)
                    mid += 1
                elif cur_sum < 0:
                    mid += 1
                else:
                    end -= 1
                    mid = start + 1

        return result


nums = [-1,0,1,2,-1,-4]
# nums = [0, 0, 0, 0]
obj = Solution()
print(obj.threeSum(nums))

