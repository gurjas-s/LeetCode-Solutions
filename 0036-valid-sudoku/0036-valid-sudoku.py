class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkGrid(subGrid, rowStart, colStart):
            seen=set()
            for i in range(rowStart, rowStart+3):
                for j in range(colStart, colStart+3):
                    if subGrid[i][j] in seen:
                        return False
                    if subGrid[i][j]!='.': seen.add(subGrid[i][j])
            return True
        n = 9
        #check if every row is valid
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[i][j] in seen:
                    return False
                if board[i][j]!='.': seen.add(board[i][j])
        #check if every column is valid
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[j][i] in seen:
                    return False
                if board[j][i]!='.': seen.add(board[j][i])
        
        #(0,0)
        #(0,3)
        #(0,6)
        #(3,0) (3,3) (3,6)
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not checkGrid(board,i,j):
                    return False
        
        return True