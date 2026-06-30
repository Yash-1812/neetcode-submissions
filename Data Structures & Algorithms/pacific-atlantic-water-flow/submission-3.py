class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac_visit = set()
        atl_visit = set()
        visited = set()
        #directions = [(1,0) , (0,1) , (-1,0) , (0,-1)]
        def pacific(i , j , r , c):
            if i >= rows or j >= cols:
                return False
            if i < 0 or j < 0:
                return True
            if heights[i][j] > heights[r][c]:
                return False
            if (i , j) in visited:
                return False
            visited.add((i , j))
            down = pacific(i + 1 , j , i , j)
            right = pacific(i , j + 1 , i , j)
            up = pacific(i - 1 , j , i , j)
            left = pacific(i , j - 1 , i , j)
            return down or right or up or left
        def atlantic(i , j , r , c):
            if i < 0 or j < 0:
                return False
            if i >= rows or j >= cols:
                return True
            if heights[i][j] > heights[r][c]:
                return False
            if (i , j) in visited:
                return False
            visited.add((i , j))
            down = atlantic(i + 1 , j , i , j)
            right = atlantic(i , j + 1 , i , j)
            up = atlantic(i - 1 , j , i , j)
            left = atlantic(i , j - 1 , i , j)
            return down or right or up or left
                

        for i in range(rows):
            for j in range(cols):
                if pacific(i , j , i , j):
                    pac_visit.add((i , j))
                visited.clear()
                if atlantic(i , j , i , j):
                    atl_visit.add((i , j))
                visited.clear()
        result = []
        for i , j in pac_visit:
            if (i , j) in atl_visit:
                result.append([i , j])
        return result