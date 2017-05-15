# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        before = None
        cur = head

        while cur is not None:
            if cur.val == val:
                if before is None:
                    head = cur.next
                    cur = cur.next
                else:
                    before.next = cur.next
                    cur = cur.next
            else:
                before = cur
                cur = cur.next

        return head


test_set = [1,2,6,3,4,5,6]
val = 6
head = None
cur = None
for i in range(len(test_set)):
    if i == 0:
        head = ListNode(test_set[i])
        cur = head

    else:
        cur.next = ListNode(test_set[i])
        cur = cur.next


cur = head
while cur is not None:
    print(cur.val, end='-')
    cur = cur.next


obj = Solution()
obj.removeElements(head, val)
print('')

cur = head
while cur is not None:
    print(cur.val, end='-')
    cur = cur.next

