class Solution:
    # @param {string} s
    # @return {integer}
    def intToRoman(self, s):
        Roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        newString = ''
        if s < 1 or s > 3999:
        	return None
        for i in range(len(num)):
        	numOfChar = s/num[i]
        	newString += Roman[i] * numOfChar
        	s -= numOfChar * num[i]
        return newString
        	
