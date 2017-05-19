class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        nums1.sort()
        nums2.sort()
        result = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return result


nums1 = [1,2,3,1]
nums2 = [5,1]

obj = Solution()
print(obj.intersection(nums1, nums2))
