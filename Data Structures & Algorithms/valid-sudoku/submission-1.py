class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #first by row
        for row in board:
            reviewed = set()
            for num in row:
                if num == '.':
                    continue
                else:
                    if num in reviewed:
                        return False
                    else:
                        reviewed.add(num)
        
        #second by column
        for j, column in enumerate(board):
            reviewed = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in reviewed:
                        return False
                    else:
                        reviewed.add(board[i][j])

        #third by square
        # 0 1 2 9 10 11 18 19
        square = 0
        while square < 9:
            reviewed = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    column = (square%3)*3 + j
                    if board[row][column] == '.':
                        continue
                    else:
                        if board[row][column] in reviewed:
                            return False
                        else:
                            reviewed.add(board[row][column])
            square +=1

        return True
        