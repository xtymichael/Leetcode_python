# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###########################  Iterative ##############################
class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        while root:
        	if max(p.val, q.val) < root.val:
        		root = root.left
        	elif min(p.val, q.val) > root.val:
        		root = root.right
        	else:
        		return root

        return None



############################   RECURSIVE ############################
class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
    	if not root or not p or not q:
    		return None
    	if (max(p.val, q.val) < root.val):
    		return self.lowestCommonAncestor(root.left, p, q)
    	elif (min(p.val, q.val) > root.val):
    		return self.lowestCommonAncestor(root.right, p, q)
    	else:
    		return root