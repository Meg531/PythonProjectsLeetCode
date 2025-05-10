'''
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
from typing import Dict
from collections import defaultdict # Importing defaultdict from collections for easier dictionary handling
from collections import Counter # Importing Counter from collections for counting hash maps

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        char_index_map: Dict[str, int] = {}  # Dictionary to store the last index of each character
        max_length = 0  # Variable to keep track of the maximum length found
        start = 0  # Start index of the current substring

        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1  # Update start index if character is found in current substring
            char_index_map[char] = i  # Update the last index of the character
            max_length = max(max_length, i - start + 1)  # Update max_length if a longer substring is found

        return max_length