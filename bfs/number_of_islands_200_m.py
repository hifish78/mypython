from collections import deque
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        cnt = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self.bfs(grid, i, j)
        return cnt

    def bfs(self, grid, i, j):
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        queue = deque()
        queue.append(Point(i, j))
        grid[i][j] == '0'

        while queue:
            cur = queue.popleft()
            for i in range(4):
                new_x = cur.x + dx[i]
                new_y = cur.y + dy[i]
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]):
                    continue
                if grid[new_x][new_y] == '1':
                    queue.append(Point(new_x, new_y))
                    grid[new_x][new_y] = '0'




