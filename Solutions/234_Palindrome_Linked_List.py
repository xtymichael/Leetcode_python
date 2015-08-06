# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head:
        	return True

        first = node = head
        temp = []

        while node:
        	temp.append(node.val)
        	node = node.next

        index = 0
        while head:
        	if head.val != temp[len(temp) - index - 1]:
        		return False
        	index += 1
        	head = head.next
        return True
