# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#IN-ORDER: LEFT -- ROOT.VAL --- RIGHT
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        self.helper(root, answer)
        return answer

    def helper(self, root, answer):
    	if root:
    		self.helper(root.left, answer)
    		answer.append(root.val)
    		self.helper(root.right, answer)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        