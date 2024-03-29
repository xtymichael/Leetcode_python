# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#https://leetcode.com/discuss/40051/3-4-lines-python
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
        	root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        	return root




#DFS
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
        	node = stack.pop()
        	if node:
        		node.left, node.right = node.right, node.left
        		stack.extend([node.left, node.right]) #stack += node.left, node.right

        return root

#BFS
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = collections.deque([(root)])
        while queue:
        	node = queue.popleft()
        	if node:
        		node.left, node.right = node.right, node.left
        		queue.append(node.left)
        		queue.append(node.right)
        return root
