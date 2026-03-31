# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # when the second pointer is None return false


        first, second = head, head

        while second and second.next:
            first = first.next
            second = second.next.next

            if second == first:
                return True
            
        
        return False
