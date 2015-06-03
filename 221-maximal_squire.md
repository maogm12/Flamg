# 221-Maximal Square

## Problem

> Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

> For example, given the following matrix:
> 
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
> Return 4.

## Solution

动规，使用二维数组dp来储存中间结果，dp[i][j]表示以（i,j）为右下角的最大正方形。那么递推式为：

	dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

## Code

### Python

```python
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        max_size = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_size = max(max_size, dp[i][j])
        return max_size * max_size
```

### C++

```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty()) {
            return 0;
        }
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        int max_size = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i-1][j-1] == '1') {
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
                    max_size = max(dp[i][j], max_size);
                }
            }
        }
        return max_size * max_size;
    }
};
```
