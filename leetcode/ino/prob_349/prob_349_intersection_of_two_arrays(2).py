class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)


nums1 = [1,2,3,1]
nums2 = [5,1]

obj = Solution()
print(obj.intersection(nums1, nums2))
