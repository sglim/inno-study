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

        num1_cur_idx = m - 1
        num2_cur_idx = n - 1
        insert_idx = num1_cur_idx + num2_cur_idx + 1

        while num2_cur_idx >= 0:
            if num1_cur_idx >= 0:
                if nums1[num1_cur_idx] > nums2[num2_cur_idx]:
                    nums1[insert_idx] = nums1[num1_cur_idx]
                    num1_cur_idx -= 1
                    insert_idx -= 1
                else:
                    nums1[insert_idx] = nums2[num2_cur_idx]
                    num2_cur_idx -= 1
                    insert_idx -= 1
            else:
                nums1[insert_idx] = nums2[num2_cur_idx]
                num2_cur_idx -= 1
                insert_idx -= 1


sol = Solution()

nums1 = [1,2,2,4]
m = len(nums1)
# m = 0

nums2 = [0,2,3]
n = len(nums2)

for i in nums2:
    nums1.append(0)

sol.merge(nums1, m, nums2, n)
print(nums1)
