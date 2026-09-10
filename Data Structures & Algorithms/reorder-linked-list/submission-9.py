# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# my try - can still be modified to get the correct answer.
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
        
#         # for n in length of list
#         Temphead = head
#         listMap = {}
#         index = 0

#         while Temphead:
#             listMap[index] = Temphead
#             index += 1
#             Temphead = Temphead.next

#         length = index
#         even = 0
#         odd = 1

        
#         for n in range(index):

#             if n % 2 == 0:
#                 head = listMap[n]
#                 even += 1
#             else:
#                 head = listMap[n-odd]
#                 odd += 1

#             head = head.next


# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         slow, fast = head, head.next

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         second = slow.next
#         prev = slow.next = None

#         # reverse list
#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp

#         # merge the two halfs of the list
#         first, second = head, prev

#         while second:
#             # next nodes in tmp variables because we're going to be breaking
#             # does links
#             tmp1, tmp2 = first.next, second.next
#             first.next = second
#             second.next = tmp1
#             first, second = tmp1, tmp2


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return

        # for n in length of list
        Temphead = head
        listMap = {}
        index = 0

        while Temphead:
            listMap[index] = Temphead
            index += 1
            Temphead = Temphead.next

        # use tow pointers to "re-stich" the list
        left, right = 0, index - 1

        while left < right:

            listMap[left].next = listMap[right]
            left += 1


            # if left and right meet at the same node (odd length)
            if left == right:
                break

            # Connect the right node to the next left node
            listMap[right].next = listMap[left]
            right -= 1

        
        # Ensure the new tail points to None, especially if the list is even
        listMap[left].next = None

        
