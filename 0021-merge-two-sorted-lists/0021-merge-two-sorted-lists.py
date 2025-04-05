# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
   
       
        arr1 = []
        arr2 = []

        cur = list1
        cur2 = list2
        while(cur!=None):
            arr1.append(cur.val)
            cur = cur.next
        while(cur2!=None):
            arr2.append(cur2.val)
            cur2 = cur2.next
        
        for elm in arr2:
            arr1.append(elm)
        
        arr1.sort()
        new_list = ListNode()
        head = new_list
        for val in arr1:
            new_node = ListNode(val, None)
            new_list.next = new_node
            new_list = new_list.next
        return head.next




        return head  
        