class Solution(object):
    # def get_best(self, cur_num, prev_sum, best_candidate, target):
    #     if abs(target - (prev_sum + cur_num)) < abs(target - best_candidate):
    #         return prev_sum + cur_num
    #     else:
    #         return best_candidate

    def get_best(self, current, candidate, target):
        if abs(target - current) > abs(target - candidate):
            return candidate
        else:
            return current

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        checker = {sum(nums[:2]): True}
        cur_sum = sum(nums[:3])

        for i in range(2, len(nums)):
            cur_num = nums[i]
            best_candidate = cur_sum

            for key in checker:
                prev_sum = key
                best_candidate = self.get_best(best_candidate, cur_num + prev_sum, target)
                if best_candidate == target:
                    return best_candidate

            cur_sum = self.get_best(cur_sum, best_candidate, target)

            for j in range(0, i):
                if nums[j] + cur_num not in checker:
                    checker[nums[j] + cur_num] = True

        return cur_sum


nums = [-1, 2, 1, -4]
target = 1

obj = Solution()
print(obj.threeSumClosest(nums, target))
