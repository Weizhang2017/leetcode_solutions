# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            node = head.next
            previous = head
            while node:
                if previous.val == node.val:
                    previous.next = node.next
                    node = node.next
                else:
                    previous, node = node, node.next
        return head

