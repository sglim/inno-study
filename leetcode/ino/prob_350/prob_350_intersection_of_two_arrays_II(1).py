class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []
        nums1_length = len(nums1)
        nums2_length = len(nums2)

        i, j, k = 0, 0, 0
        while i < nums1_length and k < nums2_length:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                nums2[k], nums2[j] = nums2[j], nums2[k]
                i += 1
                k += 1
                j = k
            else:
                j += 1
                if j == nums2_length:
                    j = k
                    i += 1

        return result


test1 = []
test2 = [1,1]

obj = Solution()
print(obj.intersect(test1, test2))
