class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        check_hash = {}
        result = []
        for num in nums1:
            if num in check_hash:
                check_hash[num] += 1
            else:
                check_hash[num] = 1

        for num in nums2:
            if num in check_hash and check_hash[num] > 0:
                result.append(num)
                check_hash[num] -= 1

        return result


test1 = []
test2 = [2,1]

obj = Solution()
print(obj.intersect(test1, test2))
