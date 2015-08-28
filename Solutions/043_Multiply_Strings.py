class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        for i in range(len(num1)):
        	result += int(num1[i]) * int(num2) * (10 ** (len(num1)- i - 1))
        return str(result)
