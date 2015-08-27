class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        stack = [0]
        area = 0

        for i in range(1, len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                area = max(area, w*h)
            stack.append(i)
        return area