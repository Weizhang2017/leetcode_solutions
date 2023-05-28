# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = {headA}
        nodeA = headA.next
        while nodeA:
            a.add(nodeA)
            nodeA = nodeA.next
        nodeB = headB
        while nodeB:
            if nodeB in a:
                return nodeB
            nodeB = nodeB.next
        return None

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head2 = ListNode(1)
    head2.next = head.next
    s = Solution()
    print(s.getIntersectionNode(head, head2))