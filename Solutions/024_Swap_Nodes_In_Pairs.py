# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        prev = self
        prev.next = head
        while prev.next and prev.next.next:
        	prev.next, prev.next.next, prev.next.next.next = prev.next.next, prev.next, prev.next.next.next
        	prev = prev.next.next
        return self.next

