# 062-Unique Paths

## Problem

> A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

> The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

> How many possible unique paths are there?
![image](./images/robot_maze.png)

> Above is a 3 x 7 grid. How many possible unique paths are there?

> Note: m and n will be at most 100.

## Solution

> 动态规划，因为机器人只能向右或者向下走，所以，到达每个空格的路径总数等于其上面和左面空格路径综述之和。即：

> dp[i][j] = dp[i-1][j] + dp[i][j-1]

## Code

### Python

```python
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
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
    int uniquePaths(int m, int n) {
        int dp[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    dp[i][j] = 1;
                    continue;
                } else {
                    dp[i][j] = 0;
                }
                if (i > 0) {
                    dp[i][j] = dp[i-1][j];
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