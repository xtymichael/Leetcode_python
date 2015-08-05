class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        maxV = 0
        for i in range(1,len(height)):
        	for j in range(i + 1, len(height) + 1):
        		if j == len(height) or (height[j - 1] <= height[j] and height[i] >= height[i-1]):
        			maxV = max(maxV, (j - i) * (height[j - 1] + height[i - 1]) / 2)
        return maxV