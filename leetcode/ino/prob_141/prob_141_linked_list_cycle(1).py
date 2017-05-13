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
        check_hash = {}
        cur = head

        while cur != None:
            if cur in check_hash:
                return True
            check_hash[cur] = True
            cur = cur.next

        return False

head = ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(5)
head.next.next.next = head

sol = Solution()
result = sol.hasCycle(head)
print(result)
