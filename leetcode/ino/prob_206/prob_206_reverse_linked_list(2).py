# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        end_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return end_node


test_list = [1,2,3,4,5]
head = None
cur = None
for i in range(len(test_list)):
    if i == 0:
        head = ListNode(test_list[i])
        cur = head
    else:
        cur.next = ListNode(test_list[i])
        cur = cur.next

cur = head
while cur is not None:
    print(cur.val, end='-')
    cur = cur.next
print('')


obj = Solution()
head = obj.reverseList(head)


cur = head
while cur is not None:
    print(cur.val, end='-')
    cur = cur.next
print('')

