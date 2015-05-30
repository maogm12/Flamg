# 200-Number of Islands

## Problem

> Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

> Example 1:
>
```
11110
11010
11000
00000
```
Answer: 1
>
Example 2:
>
```
11000
11000
00100
00011
```
Answer: 3

## Solution

每遇到一个新区域就深搜标记该区域所有点。

## Code

### Python

```python
class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        counter = 0
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, visited, i, j, m, n)
                    counter += 1
        return counter
    
    def dfs(self, grid, visited, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j] == '1' and not visited[i][j]:
            visited[i][j] = True
            self.dfs(grid, visited, i+1, j, m, n)
            self.dfs(grid, visited, i-1, j, m, n)
            self.dfs(grid, visited, i, j+1, m, n)
            self.dfs(grid, visited, i, j-1, m, n)
```

### C++

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) {
            return 0;
        }
        int m = grid.size();
        int n = grid[0].size();
        int counter = 0;
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    counter++;
                    dfs(grid, visited, i, j, m, n);
                }
            }
        }
        return counter;
    }
    
    void dfs(vector<vector<char>> &grid, vector<vector<bool>> &visited, int i, int j, int m, int n) {
        if (i < 0 || i >= m || j < 0 || j >= n) {
            return;
        }
        if (grid[i][j] == '1' && !visited[i][j]) {
            visited[i][j] = true;
            dfs(grid, visited, i+1, j, m, n);
            dfs(grid, visited, i-1, j, m, n);
            dfs(grid, visited, i, j+1, m, n);
            dfs(grid, visited, i, j-1, m, n);
        }
    }
};
```