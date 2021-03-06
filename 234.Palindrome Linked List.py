# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        tempList = list()
        while head is not None:
            
            tempList.append(head.val)
            head = head.next
           
        r = "".join(map(str,tempList[::-1]))
        l = "".join(map(str,tempList))
        
        if r == l:
            return True
        else:
            return False
            