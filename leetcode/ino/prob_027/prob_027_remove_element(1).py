class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cur_pos = 0
        cur_length = 0

        for num in nums:
            if num == val:
                continue
            else:
                nums[cur_pos] = num
                cur_pos += 1
                cur_length += 1

        return cur_length


obj = Solution()
input_arr = [3, 2, 2, 3]
val = 3

result_length = obj.removeElement(input_arr, val)
print(result_length, input_arr[:result_length])
