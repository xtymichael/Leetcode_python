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
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0
            cur.next = ListNode((value1 + value2 + carry) % 10)
            carry = (value1 + value2 + carry)/10
            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry == 1:
            cur.next = ListNode(1)
        return dummy.next