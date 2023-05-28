# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        node = head
        l.append(node.val)
        while node.next:
            node = node.next
            l.append(node.val)
        return l == l[::-1]