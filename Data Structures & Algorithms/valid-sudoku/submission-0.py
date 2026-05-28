class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        box = collections.defaultdict(list)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                box_idx = (i // 3 , j // 3)
                if val in row[i] or val in col[j] or val in box[box_idx]:
                    return False
                row[i].append(val)
                col[j].append(val)
                box[box_idx].append(val)
        return True