class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check_hash = {}

        for num in nums:
            if num in check_hash:
                return True
            else:
                check_hash[num] = True

        return False


test_arr = []

obj = Solution()
print(obj.containsDuplicate(test_arr))
