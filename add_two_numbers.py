# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodelists = [[], []]
        new_nodes_value = []
        node1 = l1
        node2 = l2
        nodelists[0].append(node1)
        nodelists[1].append(node2)
        additional = 0
        while node1.next:
            node1 = node1.next
            nodelists[0].append(node1)
        while node2.next:
            node2 = node2.next
            nodelists[1].append(node2)
        if len(nodelists[0]) < len(nodelists[1]):
            nodelists[0], nodelists[1] = nodelists[1], nodelists[0]
        new_node = None
        while nodelists[0] or nodelists[1]:
            if nodelists[0] and nodelists[1]:
                node1 = nodelists[0].pop(0)
                node2 = nodelists[1].pop(0)
                sum_ = node1.val + node2.val + additional
                if sum_ >= 10:
                    # node1.val = sum_ % 10
                    new_nodes_value.append(sum_ % 10)
                    additional = 1
                else:
                    # node1.val = sum_
                    new_nodes_value.append(sum_)
                    additional = 0
            elif nodelists[0] and not nodelists[1]:
                node1 = nodelists[0].pop()
                sum_ = node1.val + additional
                while sum_ >= 10:
                    new_nodes_value.append(sum_ % 10)
                    if node1.next:
                        node1 = node1.next
                    else:
                        
                    sum_ = node1.val + 1

                # node1.val += additional
        while new_nodes_value:
            new_node = ListNode(new_nodes_value.pop(), new_node)
        return new_node