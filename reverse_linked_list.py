# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = head
        cur_node = pre_node.next
        while cur_node:
            pre_node = cur_node
            cur_node = pre_node.next
            cur_node.next = pre_node
        return pre_node

if __name__ == '__main__':
    node0 = ListNode()
    node1 = ListNode(1, node0)
    node2 = ListNode(2, node1)

    node = node2.next
    print(node2.val)
    while node:
        print(node.val)
        node = node.next

    s = Solution()
    head = s.reverseList(node2)
    node = head.next
    print(head.val)
    while node:
        print(node.val)
        node = node.next