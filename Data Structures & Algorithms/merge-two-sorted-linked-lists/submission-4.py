# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 8, 9, 10
# 1, 4, 6
# 1, 4, 6

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newListHead = ListNode()
        newList = newListHead

        while list1 and list2 :
            
            if list1.val > list2.val:
                newList.next = list2
                list2 = list2.next
            else:
                newList.next = list1
                list1 = list1.next
            
            newList = newList.next

        
        # check which list is finished and append the remainder to the new merged
        # list

        if list2:
            newList.next = list2
        else:
            newList.next = list1
        
        return newListHead.next



