class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        for i in range(m):
            num2_min_idx = self.find_min(nums2)
            if nums1[i] > nums2[num2_min_idx]:
                nums1[i] , nums2[num2_min_idx] = nums2[num2_min_idx], nums1[i]

        #num2의 나머지를 sort 해서 num1의 index m에서부터 이어 붙인다
        for j in range(n):
            min_num = min(nums2)
            nums1[m + j] = min_num
            nums2.remove(min_num)

    def find_min(self, nums2):
        min_num = min(nums2)
        return nums2.index(min_num)


sol = Solution()

nums1 = [0]
m = len(nums1)
# m = 0

nums2 = [1]
n = len(nums2)

for i in nums2:
    nums1.append(0)

sol.merge(nums1, m, nums2, n)
print(nums1)
