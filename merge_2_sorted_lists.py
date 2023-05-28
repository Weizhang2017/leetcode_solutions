# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2:
            return list2
        elif list1 and list2 is None:
            return list1
        elif not list1 and not list2:
            return None
        
        if list1.val < list2.val:
            new_node_head = ListNode(list1.val)
            new_node = new_node_head
            list1 = list1.next
        elif list1.val == list2.val:
            new_node_head = ListNode(list1.val)
            new_node_head.next = ListNode(list2.val)
            new_node = new_node_head.next
            list2 = list2.next
            list1 = list1.next
        else:
            new_node_head = ListNode(list2.val)
            list2 = list2.next
            new_node = new_node_head

        while list1 and list2:
            # print('list1', list1.val, 'list2', list2.val)
            # print('new_node', new_node.val)
            if list1.val < list2.val:
                new_node.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val == list2.val:
                new_node.next = ListNode(list1.val)
                new_node = new_node.next
                new_node.next = ListNode(list1.val)
                list1 = list1.next
                list2 = list2.next
            else:
                new_node.next = ListNode(list2.val)
                list2 = list2.next
            new_node = new_node.next
        if list1:
            new_node.next = list1
        if list2:
            new_node.next = list2
        return new_node_head

if __name__ == '__main__':
    list_node = [[1,2,4], [1,3,4]]
    head = [ListNode(list_node[0][0]), ListNode(list_node[1][0])]
    for i in range(len(list_node)):
        node = head[i]
        for j in range(1,len(list_node[i])):
            node.next = ListNode(list_node[i][j])
            node = node.next
        node = head[i]
        # print('head: ', head[i].val)
        while node.next:
            # print(node.next.val)
            node = node.next

    s = Solution()
    new_node_head = s.mergeTwoLists(head[0], head[1])
    print('new_node_head', new_node_head.val)
    new_node = new_node_head
    print(new_node.val)
    while new_node.next:
        print(new_node.next.val)
        new_node = new_node.next