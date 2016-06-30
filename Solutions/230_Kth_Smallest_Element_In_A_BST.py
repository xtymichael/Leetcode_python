# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursive Solution
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.answer = None
        self.helper(root)
        return self.answer

    def helper(self, node):
    	if node:
    		self.helper(node.left)
    		self.k -= 1
    		if self.k == 0:
    			self.answer = node.val
    			return
    		self.helper(node.right)