# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        self.slow = head
        self.fast = head
        self.next_node = self.slow.next
        self.prev_node = None
        self.prev_node = self.slow

        self.to_left = None
        self.to_right = None

        self.result = True
        self.flag = 0  # 0 for odd list length and 1 for even list length

        while self.fast.next is not None:
            if self.fast.next.next is None:  # in case of length of list is even
                self.flag = 1
                break

            self.fast = self.fast.next.next

            self.slow = self.next_node
            self.next_node = self.slow.next
            self.slow.next = self.prev_node
            self.prev_node = self.slow

        head.next = None

        self.to_right = self.next_node
        # 1. 짝수일 경우 : left = slow, right = next_node
        if self.flag:
            self.to_left = self.slow

        # 2. 홀수일 경우 : (가운데 수는 버리고) left = slow.next, right = next_node
        else:
            self.to_left = self.slow.next

        while self.to_left is not None:
            if self.to_left.val != self.to_right.val:
                self.result = False
                break

            self.to_left = self.to_left.next
            self.to_right = self.to_right.next

        return self.result


test_arr = [1,2,3,3,2,1,9]
head = None
cur = None

for i in range(len(test_arr)):
    if i == 0:
        head = ListNode(test_arr[i])
        cur = head
    else:
        cur.next = ListNode(test_arr[i])
        cur = cur.next


cur = head
while cur is not None:
    print(cur.val, end='-')
    cur = cur.next
print('')


obj = Solution()
print(obj.isPalindrome(head))
