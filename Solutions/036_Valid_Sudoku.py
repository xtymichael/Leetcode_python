class Solution:
    # @param {character[][]} board
    # @return {boolean}
	def isValidSudoku(self, board):
		for i in range(9):
			row = self.checklist(board[i][:])  #passed a string
			if not row:
				return False

		for a in range(9):
			col = self.checklist([r[a] for r in board])  # passed a list
			if not col:
				return False

		for l in range(3):
			for m in range(3):
				temp = ''
				for j in range(3*l,3*l+3):
					for k in range(3*m,3*m+3):
						temp += board[j][k]
				block = self.checklist(temp)  #passed a string
				if not block:
					return False

		return True

	def checklist(self, clist):
		total = ['1','2','3','4','5','6','7','8','9']
		for ch in clist:
			if ch != '.':
				if ch not in total:
					return False
				total.pop(total.index(ch))
		return True