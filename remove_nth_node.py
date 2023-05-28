# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 1
        node = head
        while node.next:
            counter += 1
            node = node.next

        if n == counter:
            head = head.next
            return head
            
        node = head
        while True:
            if counter == n+1:
                node.next = node.next.next
                break
            node = node.next
            counter -= 1

        return head
