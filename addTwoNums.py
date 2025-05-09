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

'''
### Explanation of Your Code

Your code implements a solution to add two numbers represented as linked lists. Each digit of the numbers is stored in reverse order in the linked lists, and the result is also returned as a linked list in reverse order.

#### Key Components:
1. **`ListNode` Class**:
   - Represents a node in a singly linked list.
   - Each node contains a value (`val`) and a pointer to the next node (`next`).

2. **`add_two_nums` Method**:
   - This method is part of the `Solution` class and performs the addition of two numbers represented by linked lists.
   - **Steps**:
     - A dummy node (`dummy`) is used to simplify the process of building the result linked list.
     - A `carry` variable is used to handle cases where the sum of two digits exceeds 9.
     - A `while` loop iterates through the nodes of `l1` and `l2` until both are exhausted and there is no carry left.
     - At each step:
       - The values of the current nodes of `l1` and `l2` are added along with the carry.
       - A new node is created with the value of the current digit (`total % 10`), and the carry is updated (`total // 10`).
       - The pointers `l1` and `l2` are moved to their respective next nodes.
     - Finally, the method returns `dummy.next`, which points to the head of the result linked list.

3. **Helper Functions**:
   - `create_linked_list`: Converts a Python list into a linked list.
   - `print_linked_list`: Converts a linked list back into a Python list for easy visualization.

4. **Test Cases**:
   - Two linked lists (`l1` and `l2`) are created to represent the numbers 342 and 465.
   - The `add_two_nums` method is called to compute their sum, and the result is printed.

---

### Time Complexity (O Notation)

1. **`add_two_nums` Method**:
   - The `while` loop iterates through the nodes of `l1` and `l2` until both are exhausted.
   - Let `n` and `m` be the lengths of `l1` and `l2`, respectively.
   - The loop runs for `max(n, m)` iterations.
   - **Time Complexity**: **O(max(n, m))**

2. **`create_linked_list` and `print_linked_list` Functions**:
   - Both functions iterate through the list of values or the linked list once.
   - **Time Complexity**: **O(k)**, where `k` is the number of elements in the list or linked list.

3. **Overall Complexity**:
   - The overall complexity of the program is dominated by the `add_two_nums` method.
   - **Overall Time Complexity**: **O(max(n, m))**

---

### Space Complexity

1. **`add_two_nums` Method**:
   - A new linked list is created to store the result.
   - The space required is proportional to the number of nodes in the result linked list.
   - **Space Complexity**: **O(max(n, m))**

2. **Helper Functions**:
   - The `create_linked_list` function uses a dummy node and a pointer, which are constant space.
   - The `print_linked_list` function uses a list to store the values, which requires **O(k)** space.

3. **Overall Space Complexity**:
   - **O(max(n, m))**

---

### Summary

- **Time Complexity**: **O(max(n, m))**
- **Space Complexity**: **O(max(n, m))**
- The code is efficient and works well for the problem of adding two numbers represented as linked lists. It handles edge cases like different lengths of `l1` and `l2` and carries overflows correctly.

For LeetCode, the code is ready to be submitted as it meets the problem requirements and passes the test cases.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
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
'''