# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        hA = headA
        hB = headB
        lengthA = 0
        lengthB = 0

        while hA:
            lengthA += 1
            hA = hA.next

        while hB:
            lengthB += 1
            hB = hB.next

        while headA and headB:
            if headA == headB:
                return headA
            elif lengthA >= lengthB:
                headA = headA.next
                lengthA -= 1
            else:
                headB = headB.next
                lengthB -= 1
        return None