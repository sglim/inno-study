'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example,
Given nums = [0, 1, 3] return 2.


if array has all numbers 0 ~ n, its sum should be : n(n+1) / 2
thus difference between n(n+1)/2 and real sum should be a missing number.

* get array length, n : ~O(n)
* calculate n(n+1)/2 : ~O(1)
* sum array : ~O(n)

* time complexity : ~O(n)

'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return int(n * (n+1) / 2 - sum(nums))


nums = [0,1,2]
obj = Solution()
print(obj.missingNumber(nums))


