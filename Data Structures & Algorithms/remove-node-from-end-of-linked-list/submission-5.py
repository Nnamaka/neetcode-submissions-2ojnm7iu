# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp_head = head
        listMap = {}
        index = 0

        while temp_head:
            listMap[index] = temp_head
            temp_head = temp_head.next
            index += 1

        remove = index - n

        # if we are to remove the head node
        if remove == 0:
            return head.next
        
        # case to handle if we want to remove the last node
        if remove + 1 in listMap:
            listMap[remove - 1].next = listMap[remove+1]
        else:
            listMap[remove - 1].next = None

        # you may clean up the dictionary
        listMap.pop(remove)

        return head


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
#         dummy = ListNode(0, head)
#         left = dummy
#         right = head

#         # put the right pointer at the position 0 + 2
#         while n > 0 and right:
#             right = right.next
#             n -= 1

#         while right:
#             left = left.next
#             right = right.next

#         # delete node
#         left.next = left.next.next

#         return dummy.next
