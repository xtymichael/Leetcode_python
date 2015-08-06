# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
    	prev, cur, prev.next = self, head, head
    	while cur:
    		if not cur.next or cur.next.val != cur.val:
    			prev.next = cur
    			prev = prev.next
    		else:
    			while cur.next and cur.next.val == cur.val:
    				cur = cur.next
    			prev.next = cur.next
    		cur = cur.next
    	return self.next





