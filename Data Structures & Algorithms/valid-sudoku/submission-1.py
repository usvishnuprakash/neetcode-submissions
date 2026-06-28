class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)

        
        for row in board:
            seen = set()
            for col in row:

                if col == ".":
                    continue 

                if col in seen:
                    return False

                seen.add(col)

        # column
        
        for col in range(n) :
            seen= set()

            for row in range(n):
                colval=  board[row][col]

                if colval == ".":
                    continue

                if colval in seen:
                    return False
                
                seen.add(colval)
        
        # in box

        for row_start in range(0,n,3):
            for col_start in range (0,n,3):

                seen = set()
                for row in  range(row_start,row_start+3):

                    for col in range(col_start,col_start+3):
                        colval = board[row][col]

                        if colval == ".":
                            continue

                        if colval in seen:
                            return False

                        seen.add(colval)
        
        return True














                