# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        cur_val = head.val
        cur = head

        while cur.next is not None:
            while cur.next is not None and cur.next.val == cur_val:
                self.delete_next(cur)
            if cur.next is not None:
                cur = cur.next
                cur_val = cur.val

        return head

    def delete_next(self, cur):
        next_node = cur.next
        cur.next = next_node.next
        del next_node


def array_to_list(arr):
    head = ListNode(arr[0])
    cur = head

    for input_num in arr[1:]:
        cur.next = ListNode(input_num)
        cur = cur.next

    return head


def print_list(head):
    cur = head
    while cur is not None:
        print(cur.val,'*** ',end='')
        cur = cur.next
    print('')


test_input = [1,1,2,3,3]
test_head = array_to_list(test_input)
sol = Solution()

print_list(test_head)
output_head = sol.deleteDuplicates(test_head)
print_list(output_head)
