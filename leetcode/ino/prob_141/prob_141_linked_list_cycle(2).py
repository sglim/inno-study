# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is not None and head.next is not None:
            slow = head
            fast = head.next
        else:
            return False

        while slow is not None and fast is not None:
            if slow == fast:
                return True

            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next

        return False

head = ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(5)
# head.next.next.next.next = ListNode(6)


sol = Solution()
result = sol.hasCycle(head)
print(result)
