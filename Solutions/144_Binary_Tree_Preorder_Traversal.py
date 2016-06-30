# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



#PRE ORDER: ROOT --- LEFT ---- RIGHT

#Recursive
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        self.helper(root, answer)
        return answer

    def helper(self, root, answer):
    	if root:
    		answer.append(root.val)
    		self.helper(root.left, answer)
    		self.helper(root.right, answer)



#Iteratively
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        

