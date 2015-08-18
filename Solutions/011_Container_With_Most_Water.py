class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
    	first = 0
    	last = len(height) - 1
    	maxV = 0

    	while first < last:
    		maxV = max(min(height[first], height[last]) * (last - first), maxV)
    		if height[first] < height[last]:
    			first += 1
    		else:
    			last -= 1
    	return maxV

