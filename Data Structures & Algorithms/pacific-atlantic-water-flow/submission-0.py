class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atlan = set(), set()
        rows, cols = len(heights), len(heights[0])
        neighbour = [[-1,0], [1, 0], [0, -1], [0, 1]]
        def dfs(i: int, j: int, edge: str):
            if edge == "pacific" and (i, j) in pac:
                return
            elif edge == "atlantic" and (i, j) in atlan:
                return
            if edge == "pacific":
                pac.add((i, j))
            else:
                atlan.add((i, j))
            
            for nh in neighbour:
                r, c = i + nh[0], j + nh[1]
                if 0 <= r < rows and 0 <= c < cols and heights[i][j] <= heights[r][c]:
                    dfs(r, c, edge)
            return
        for r in range(rows):
            dfs(r, 0, "pacific")
            dfs(r, cols-1, "atlantic")
        for c in range(cols):
            dfs(0, c, "pacific")
            dfs(rows-1, c, "atlantic")
        return list(pac & atlan)
