# 063-Unique Paths II

## Problem

> Follow up for "Unique Paths":

> Now consider if some obstacles are added to the grids. How many unique paths would there be?

> An obstacle and empty space is marked as 1 and 0 respectively in the grid.

> For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
>
```
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
```
The total number of unique paths is 2.

> **Note**: m and n will be at most 100.

## Solution

动态规划，与062题目差不多，当前空格与其左边空格和上面空格的路径数目相关。

不同的地方在于，当一个地方是障碍物时，首先，需要将其路径数目设为0.

## Code

### Python

```python
class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                else:
                    dp[i][j] = 0

                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]
```

### C++

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        int dp[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                    continue;
                }
                if (i == 0 && j == 0) {
                    dp[i][j] = 1;
                    continue;
                } else {
                    dp[i][j] = 0;
                }

                if (i > 0) {
                    dp[i][j] += dp[i-1][j];
                }
                if (j > 0) {
                    dp[i][j] += dp[i][j-1];
                }
            }
        }
        return dp[m-1][n-1];
    }
};
```

dp's Memoization

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int height = obstacleGrid.size();
        if (height == 0) return 0;
        int width = obstacleGrid[0].size();
        if (width == 0) return 0;
        if (obstacleGrid[0][0] == 1 || obstacleGrid[height - 1][width - 1] == 1) return 0;
        vector<vector<int>> pathNum(height, vector<int>(width, -1));
        pathNum[0][0] = 1;
        return uniquePathsWithObstacles(obstacleGrid, pathNum, height - 1, width - 1);
    }

    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid, vector<vector<int>>& pathNum, int i, int j) {
        if (pathNum[i][j] == -1) {
            pathNum[i][j] = 0;
            if (i > 0 && obstacleGrid[i - 1][j] == 0) {
                pathNum[i][j] += uniquePathsWithObstacles(obstacleGrid, pathNum, i - 1, j);
            }
            if (j > 0 && obstacleGrid[i][j - 1] == 0) {
                pathNum[i][j] += uniquePathsWithObstacles(obstacleGrid, pathNum, i, j - 1);
            }
        }
        return pathNum[i][j];
    }
};
```
