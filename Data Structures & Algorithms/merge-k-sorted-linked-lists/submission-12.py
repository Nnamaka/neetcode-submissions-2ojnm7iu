# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists or len(lists) == 0:
#             return None

#         while len(lists) > 1:
#             mergedList = []

#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if (i + 1) < len(lists) else None

#                 mergedList.append(self.mergeList(l1, l2))
#             lists = mergedList

#         return lists[0]


#     def mergeList(self, l1, l2):

#         dummy = ListNode()
#         tail = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next

#             tail = tail.next
        
#         if l1:
#             tail.next = l1
#         if l2:
#             tail.next = l2

#         return dummy.next






# Making Divide and Conquer O(1) Space

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None


        list_node_values = defaultdict(list)
        new_list = ListNode()
        iterate_list = new_list
        res = []

        for item in lists:
            while item:
                list_node_values[item.val].append(item)
                item = item.next
        # { 1: [ object, object2], 2: [object1, object2]}

        for i in sorted(list_node_values.keys()):
            while  len(list_node_values[i]) != 0:
                iterate_list.next = list_node_values[i].pop(0)
                iterate_list = iterate_list.next

        iterate_list.next = None
        return new_list.next








