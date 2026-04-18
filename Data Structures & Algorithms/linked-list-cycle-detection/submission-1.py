# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slo, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slo = slo.next
            if slo == fast: return True
        return False
