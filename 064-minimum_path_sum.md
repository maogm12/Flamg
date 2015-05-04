# 064-Minimum Path Sum

## Problem

> Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

> **Note**: You can only move either down or right at any point in time.

## Solution

到达当前坐标位置的最小和路径只有两个来源，即上方和左方。所以，递推式为
`dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]`

## Code

### Python

```python
class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[m-1][n-1]
```

### C++

```cpp
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        for (int j = 1; j < n; j++) {
            grid[0][j] += grid[0][j-1];
        }
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i-1][0];
            for (int j = 1; j < n; j++) {
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        return grid[m-1][n-1];
    }
};
```