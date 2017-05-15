# by cyclic replacement

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        count = 0
        start = 0

        while count < length:
            current = start
            prev = nums[start]

            next_idx = (current + k) % length
            temp = nums[next_idx]
            nums[next_idx] = prev
            prev = temp

            current = next_idx
            count += 1

            while start != current:
                next_idx = (current + k) % length
                temp = nums[next_idx]
                nums[next_idx] = prev
                prev = temp

                current = next_idx
                count += 1

            start += 1


test_arr = [1,2,3,4,5,6,7]
k = 3

obj = Solution()
obj.rotate(test_arr, k)

print(test_arr)
