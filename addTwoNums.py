""" Definition for singly-linked list.
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def add_two_nums(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented by two linked lists and return the sum as a linked list.

        Args:
            l1 (Optional[ListNode]): The first linked list representing a number.
            l2 (Optional[ListNode]): The second linked list representing a number.

        Returns:
            Optional[ListNode]: A linked list representing the sum of the two numbers.
        """
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Helper function to print a linked list as a list of values."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Test cases
l1 = create_linked_list([2, 4, 3])  # Represents 342
l2 = create_linked_list([5, 6, 4])  # Represents 465

solution = Solution()
result = solution.add_two_nums(l1, l2)

# Print the result
print_linked_list(result)  # Expected output: [7, 0, 8] (Represents 807)