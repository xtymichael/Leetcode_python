# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1:
        	return l2
        if not l2:
        	return l1
        carry = (l1.val + l2.val)/10
        digit = (l1.val + l2.val)%10