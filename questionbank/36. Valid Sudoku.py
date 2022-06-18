from cProfile import label
from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        const_row_len=9
        const_col_len=9
        cols=defaultdict(lambda:set())
        rows=defaultdict(lambda:set())
        grids=defaultdict(lambda:set())
        for ri in range(0,const_row_len):
            for cj in range(0,const_col_len):
                if board[ri][cj]==".":
                    continue
                num=board[ri][cj]
                if num in rows[ri]:
                    return False 
                if num in cols[cj]:
                    return False 
                if num in grids[(ri//3)*3+cj//3]:
                    return False 
                rows[ri].add(num)
                cols[cj].add(num)
                grids[(ri//3)*3+cj//3].add(num) # 比较妙的地方，下取整，然后再乘以权值
        return True 


