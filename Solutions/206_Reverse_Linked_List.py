######################### prev, cur, next node #####################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            temp = cur.next # save cur.next node to a temp node
            cur.next = prev
            prev = cur
            cur = temp
        return prev

########### recursive solution #####################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return newhead 




