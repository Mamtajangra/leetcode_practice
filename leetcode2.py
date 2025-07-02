
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        head = dummy
        carry = 0
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            total = l1val + l2val + carry

            carry = total // 10
            nodeval = total % 10

            newnode = ListNode(val = nodeval)

            dummy.next = newnode
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head.next

if __name__ == "__main__":
    # Helper function to create a linked list from a list of integers
    def create_linked_list(lst):
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    # Helper function to print a linked list
    def print_linked_list(node):
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        print(" -> ".join(vals))

    # Example input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    test1 = Solution()
    result = test1.addTwoNumbers(l1, l2)
    print_linked_list(result)