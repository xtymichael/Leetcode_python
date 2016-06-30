class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board_cp = [b[:] for b in board]
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
        	for j in range(cols):
        		total = self.getStatus(board_cp,i,j)
        		if board[i][j]:
        			if total > 3 or total < 2:
        				board[i][j] = 0
        		else:
        		    if total == 3:
        				board[i][j] = 1
    
    def getStatus(self, board_cp, i, j):
    	rows = len(board_cp)
    	cols = len(board_cp[0])
    	total = 0
    	if i > 0 and j > 0:
    		total += board_cp[i-1][j-1]
    	if i > 0:
    		total += board_cp[i-1][j]
    	if i > 0 and j < cols - 1:
    		total += board_cp[i-1][j+1]
    	if j > 0:
    		total += board_cp[i][j-1]
    	if j < cols -1:
    		total += board_cp[i][j+1]
    	if i < rows - 1 and j > 0:
    		total += board_cp[i+1][j-1]
    	if i < rows - 1:
    		total += board_cp[i+1][j]
    	if i < rows - 1 and j < cols - 1:
    		total += board_cp[i+1][j+1]
    	return total

