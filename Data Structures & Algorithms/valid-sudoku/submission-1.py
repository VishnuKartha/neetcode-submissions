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
 squares 0 => 9

 square_idx 3 has a row, col 3,0 

               row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    square 0
                    0 // 3 = 0 
                    0 % 3 = 0
                    1 // 3 = 0
                    1 % 3 = 1
                    2 // 3 = 0
                    2 % 3 = 2
                    3 // 3 = 1 
                    3 % 3 = 0

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




Idea keep 3 maps which contain sets

rows {0:{}, 1: {} ... 9: {}}
cols {0:{}, 1: {} ... 9: {}}
squares {(0,0):{}, (0,1): {} ... (2,2): {}}

[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"], idx (7,8) should map to square (2,2) 7//3 = 2 8//3 =2
 [".",".",".",".","8",".",".","7","9"]]

 iterate through each element and populate t[he 3 entries that tile has membership to

 for [i,j]
 it maps to the sets rows[i], cols[j], and squares[(i//3), (j //3))]



"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in cols[j]:
                        return False
                    if board[i][j] in squares[(i//3,j//3)]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(i//3,j//3)].add(board[i][j])
        return True
        

        
        


        