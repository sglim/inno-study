# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        result_list = None
        result_cur = result_list

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                if result_cur is None:
                    result_list = l1
                else:
                    result_cur.next = l1
                result_cur = l1
                l1 = l1.next
            else:
                if result_cur is None:
                    result_list = l2
                else:
                    result_cur.next = l2
                result_cur = l2
                l2 = l2.next

        while l1 is not None:
            result_cur.next = l1
            result_cur = l1
            l1 = l1.next

        while l2 is not None:
            result_cur.next = l2
            result_cur = l2
            l2 = l2.next

        return result_list




test_input_1 = [3,6,9]
test_input_2 = [1,1,5,8]


###############
test_l1 = ListNode(test_input_1[0])
test_l1_cur = test_l1

for data in test_input_1[1:]:
    new_node = ListNode(data)
    test_l1_cur.next = new_node
    test_l1_cur = test_l1_cur.next


test_l1_cur = test_l1

while test_l1_cur is not None:
    print(test_l1_cur.val,'** ',end='')
    test_l1_cur = test_l1_cur.next


print('')
###############



test_l2 = ListNode(test_input_2[0])
test_l2_cur = test_l2

for data in test_input_2[1:]:
    new_node = ListNode(data)
    test_l2_cur.next = new_node
    test_l2_cur = test_l2_cur.next


test_l2_cur = test_l2
while test_l2_cur is not None:
    print(test_l2_cur.val,'** ',end='')
    test_l2_cur = test_l2_cur.next


print('')
#################


sol = Solution()
result_list = sol.mergeTwoLists(test_l1, test_l2)

result_cur = result_list
while result_cur is not None:
    print(result_cur.val,'** ',end='')
    result_cur = result_cur.next


