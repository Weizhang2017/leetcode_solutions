# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            node = head.next
            node_list = set()
            while node:
                if node not in node_list:
                    node_list.add(node)
                    node = node.next
                else:
                    return True
        return False

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print(head.next == head.next.next.next)
    s = Solution()
    print(s.hasCycle(head))