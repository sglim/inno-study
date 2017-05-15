# by reverse array

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


test_arr = [1,2,3,4,5,6,7]
k = 3

obj = Solution()
obj.rotate(test_arr, k)

print(test_arr)
