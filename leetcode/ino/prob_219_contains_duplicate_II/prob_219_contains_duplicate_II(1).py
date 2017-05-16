class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        check_hash = {}
        for i in range(len(nums)):
            if nums[i] in check_hash:
                j = check_hash[nums[i]]
                if i - j <= k:
                    return True
                else:
                    check_hash[nums[i]] = i
            else:
                check_hash[nums[i]] = i

        return False


test_arr = [] # [1,2,3,4,5,6,1]
k = 0

obj = Solution()
print(obj.containsNearbyDuplicate(test_arr, k))
