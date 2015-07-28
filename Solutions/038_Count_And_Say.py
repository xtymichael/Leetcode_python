class Solution:
	# @param {integer} n
	# @return {string}
	def countAndSay(self, n):
		newN = '1'
		for j in range(n - 1):
			newN = self.getNextSeq(newN)
		return newN

	def getNextSeq(self, s): 
		temp = []
		newS = ''
		for i in range(len(s)):
			#when list is empty, put it in the list
			if not temp:              
				temp.append(s[i])

			#when the char is not in list, add it to result   222 --->32
			elif s[i] not in temp:
				newS += str(len(temp))+ str(temp[0])
				temp = [s[i]]

			#when char is in list, keep counting
			elif s[i] in temp:
				temp.append(i)

			#when reach the last char, add it to result
			if i == len(s) - 1:
				newS += str(len(temp))+ str(temp[0])
				
		return newS






