# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
    	dummy = ListNode(0)
    	dummy.next = head
    	prev, current = dummy, head
    	while (current):
    		if current.val == val:
    			prev.next = current.next
    			current = current.next
    		else:
    			prev, current = current, current.next
    	return dummy.next