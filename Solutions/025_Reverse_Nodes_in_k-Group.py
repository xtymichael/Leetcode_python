# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        node = head
        length = 0
        while (node):
        	length += 1
        	node = node.next
        if not head or k <= 1 or k >= length:
        	return head

        dummy = self
        dummy.next = head
        cur = head

        for i in range(0, length/k * k, k):
        	number = k
        	while number > 0:

        		if number == n:

        		temp = cur.next
        		temp.next = cur
