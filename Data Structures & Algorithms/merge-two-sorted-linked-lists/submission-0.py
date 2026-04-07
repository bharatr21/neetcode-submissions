# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        node = dummy
        l1, l2 = list1, list2
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next
        while l1:
            node.next = ListNode(l1.val)
            l1 = l1.next
            node = node.next
        while l2:
            node.next = ListNode(l2.val)
            l2 = l2.next
            node = node.next

        return dummy.next