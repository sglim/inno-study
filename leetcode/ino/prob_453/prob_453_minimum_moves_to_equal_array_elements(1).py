# time limit fail

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        min_val = min(nums)

        count = 0
        while max_val != min_val:
            flag = True
            for i in range(len(nums)):
                if nums[i] == max_val and flag:
                    flag = False
                else:
                    nums[i] += 1
            count += 1
            max_val = max(nums)
            min_val = min(nums)

        return count


input_arr = [1, 2, 3]
obj = Solution()
print(obj.minMoves(input_arr))
