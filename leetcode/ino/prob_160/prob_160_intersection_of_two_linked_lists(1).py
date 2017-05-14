# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
        """
        if headA is None or headB is None:
            return None

        pointer_a = headA
        pointer_b = headB
        temp_end = None

        while pointer_a != pointer_b:
            if pointer_a.next is None and pointer_b.next is None:
                if pointer_a != pointer_b:
                    return None
                else:
                    pointer_a = headB
                    pointer_b = headA
                    continue
            else:
                if pointer_a.next is None:
                    if temp_end is not None and temp_end != pointer_a:
                        return None
                    else:
                        temp_end = pointer_a
                        pointer_a = headB
                        pointer_b = pointer_b.next
                        continue

                if pointer_b.next is None:
                    if temp_end is not None and temp_end != pointer_b:
                        return None
                    else:
                        temp_end = pointer_b
                        pointer_b = headA
                        pointer_a = pointer_a.next
                        continue

            pointer_a = pointer_a.next
            pointer_b = pointer_b.next

        return pointer_a


test_a = [1, 3]
test_b = [2, 4]

headA = ListNode(test_a[0])
cur = headA
for num in test_a[1:]:
    cur.next = ListNode(num)
    cur = cur.next
cur = headA
while cur != None:
    print(cur.val,end=' ')
    cur = cur.next

print('')

headB = ListNode(test_b[0])
cur = headB
for num in test_b[1:]:
    cur.next = ListNode(num)
    cur = cur.next
cur = headB
while cur != None:
    print(cur.val,end=' ')
    cur = cur.next

print('')

obj = Solution()
result = obj.getIntersectionNode(headA, headB)
if result is None:
    print(result)
else:
    print(result, result.val)
