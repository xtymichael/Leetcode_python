# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        first = head
        length = 0
        while (first):
        	first = first.next
        	length += 1

        if length == n:
        	return head.next

        result = head
        for i in range(length - n - 1):
        	result = result.next
        result.next = result.next.next
        return head


