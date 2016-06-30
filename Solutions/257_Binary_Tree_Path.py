# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
        	return []
        answer = []
        self.dfs(root, "", answer)
        return answer

    def dfs(self, root, ls, answer):
    	if not root.left and not root.right:
    		answer.append(ls + str(root.val))
    	if root.left:
    		self.dfs(root.left, ls + str(root.val) + "->", answer)
    	if root.right:
    		self.dfs(root.right, ls + str(root.val) + "->", answer)
