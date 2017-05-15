class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_idx = len(nums) - 1
        lower = nums[:last_idx - k + 1]
        higher = nums[last_idx - k + 1:]
        nums[:] = higher + lower


test_arr = [1,2,3,4,5,6,7]
k = 3

obj = Solution()
obj.rotate(test_arr, k)

print(test_arr)
