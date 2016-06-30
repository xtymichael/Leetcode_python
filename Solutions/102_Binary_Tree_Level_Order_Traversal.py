# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level 1 --- level 2 ----....

#Iter solution 1
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer = []

        level = [root]

        while root and level:
        	currentNodes = []
        	nextLevel = []
        	for node in level:
        		currentNodes.append(node.val)
        		if node.left:
        			nextLevel.append(node.left)
        		if node.right:
        			nextLevel.append(node.right)
        	answer.append(currentNodes)
        	level = nextLevel

        return answer

#iter solution 2
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer, level = [], [root]
        while root and level:
        	answer.append([node.val for node in level])
        	LRpair = [(node.left, node.right) for node in level] #get each node left right
        	level = [leaf for LR in LRpair for leaf in LR if leaf] # put all the leaves to next level
        return answer