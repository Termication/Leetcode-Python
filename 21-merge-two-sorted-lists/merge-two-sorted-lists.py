# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node to simplify handling the head of the merged list.
        dummy = ListNode(0)

        # 'current' pointer will be used to build the merged list.
        current = dummy

        # Pointers for traversing list1 and list2.
        p1 = list1
        p2 = list2

        # Iterate while both lists have nodes to compare.
        while p1 is not None and p2 is not None:
            # Compare the values of the current nodes in both lists.
            if p1.val <= p2.val:
                # If p1's value is smaller or equal, append p1's node to the merged list.
                current.next = p1
                # Move the pointer in list1 forward to the next node.
                p1 = p1.next
            else:
                # If p2's value is smaller, append p2's node to the merged list.
                current.next = p2
                # Move the pointer in list2 forward to the next node.
                p2 = p2.next

            # Move the 'current' pointer in the merged list forward
            # to the node that was just appended.
            current = current.next

        # After the loop, one of the lists might still have remaining nodes.
        # Since both original lists were sorted, the remaining nodes
        # are all greater than or equal to the last node added to the merged list.
        # Append the rest of the non-empty list to the merged list.
        if p1 is not None:
            current.next = p1
        elif p2 is not None:
            current.next = p2

        # The merged list starts after the dummy node. Return the next node of dummy.
        return dummy.next