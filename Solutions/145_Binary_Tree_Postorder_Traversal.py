# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# POST ORDER:  LEFT --- RIGHT ---- ROOT.VAL
class Solution(object):
    def postorderTraversal(self, root):
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
    		self.helper(root.right, answer)
    		answer.append(root.val)