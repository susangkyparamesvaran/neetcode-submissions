class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check each row
        for i in range(0,9):
            row = {}
            for j in range(0,9):
                if board[i][j] == ".":
                    continue        
                elif (board[i][j]) in row:
                    return False
                else:
                    row[board[i][j]] = True
        
        # check each column
        for i in range(0,9):
            column = {}
            for j in range(0, 9):
                if board[j][i] == ".":
                    continue
                elif (board[j][i]) in column:
                    return False
                else:
                    column[board[j][i]] = True

        # check each box
        for square in range(0,9):
            box = {}
            for i in range(0,3):
                for j in range(0,3):
                    row = (square // 3) * 3 + i
                    column = (square % 3) * 3 + j

                    if board[row][column] == ".":
                        continue  
                    elif board[row][column] in box:
                        return False
                    else:
                        box[board[row][column]] = True
                
        return True
