# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        1 - 2 - 3
        """
        if not head:
            return False

        fast = head
        slow = head
        count = 0
        while(True):
            if fast.next is None:
                return False
 
            fast = fast.next
            count += 1
            if count == 2:
                count = 0 
                slow = slow.next
            if slow.val == fast.val and slow.next==fast.next:
                return True


