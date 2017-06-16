# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = None
        result_cur = result
        l1_cur, l2_cur = l1, l2
        a, b, carry, sum = 0, 0, 0, 0

        while l1_cur is not None or l2_cur is not None:
            if l1_cur is None:
                a = 0
            else:
                a = l1_cur.val
                l1_cur = l1_cur.next

            if l2_cur is None:
                b = 0
            else:
                b = l2_cur.val
                l2_cur = l2_cur.next

            sum = (a + b + carry)
            carry = int(sum / 10)
            sum = int(sum % 10)

            if result_cur is None:
                result = ListNode(sum)
                result_cur = result
            else:
                result_cur.next = ListNode(sum)
                result_cur = result_cur.next

        if carry:
            result_cur.next = ListNode(carry)

        return result


######test######

arr1 = [0]
arr2 = [5, 6, 4]

list_1 = None
list_1_cur = list_1
for num in arr1:
    if list_1_cur is None:
        list_1 = ListNode(num)
        list_1_cur = list_1
    else:
        list_1_cur.next = ListNode(num)
        list_1_cur = list_1_cur.next

list_2 = None
list_2_cur = list_2
for num in arr2:
    if list_2_cur is None:
        list_2 = ListNode(num)
        list_2_cur = list_2
    else:
        list_2_cur.next = ListNode(num)
        list_2_cur = list_2_cur.next

# print
cur = list_1
while cur is not None:
    print(cur.val, end='-')
    cur = cur.next

print('')

cur = list_2
while cur is not None:
    print(cur.val, end='-')
    cur = cur.next

print('')

obj = Solution()
ans = obj.addTwoNumbers(list_1, list_2)

cur = ans
while cur is not None:
    print(cur.val, end='-')
    cur = cur.next