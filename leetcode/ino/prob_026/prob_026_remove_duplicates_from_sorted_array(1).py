class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 1:
            return 0

        cur_length = 1
        cur_pos = 1
        cur_num = nums[0]

        for num in nums[1:]:
            if num == cur_num:
                continue
            else:
                cur_length += 1
                cur_num = num
                nums[cur_pos] = num
                cur_pos += 1

        return cur_length


obj = Solution()
input_arr = [1, 1, 2]
print(obj.removeDuplicates(input_arr), input_arr)
