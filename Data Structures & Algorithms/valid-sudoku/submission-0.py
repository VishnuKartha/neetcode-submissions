"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


 Idea simple brute force algorithm. Check if theres a duplicate in all rows, then all columns then all 3x 3

[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
 board[i][j]= r rows by c columns

 step 1 iterate through rows
 board[i][0] - board[i][9] for i  in 0 - 9 check each row for duplicates

 step 2 iterate through columns
 board[0][j] - board[9][j] for j in 0 - 9 check each column for duplicates

 step 3 iterate through the 3x3s how to iterate through a 3x3
 let x,y be the top left corner of each 3 by 3
 the three by 3 is the following rows 
 [board[x][y]: board[x][y+3]] | [board[x+1][y]: board[x+1][y+3]] |[board[x+2][y]: board[x+2][y+3]]

 values of x,y : 0,0, 0,3  0,6  3,0 3,3 3,6 6,0 6,3 6,6


"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board) # 9 
        c = len(board[0]) # 9 
        for i in range(r):
            seen_before = set() #{1,2,}
            for j in range(c):
                if board[i][j] in seen_before: 
                    return False
                if board[i][j] != ".":
                    seen_before.add(board[i][j])
        for j in range(c):
            seen_before = set()
            for i in range(r):
                if board[i][j] in seen_before: 
                    return False
                if board[i][j] != ".":
                    seen_before.add(board[i][j])
        for i in range (3):
            for j in range(3):
                x = 3 * i
                y = 3 * j
                seen_before = set()
                for a in range(3):
                    for b in range(3):
                        if board[a + x][b + y] in seen_before: 
                            return False
                        if board[a + x][b + y] != ".":
                            seen_before.add(board[a + x][b+y])
        return True

        
        


        