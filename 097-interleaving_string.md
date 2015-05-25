# 097-Interleaving String

## Problem

> Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

> For example,
Given:

> s1 = `"aabcc"`,
> 
> s2 = `"dbbca"`,

> When s3 = `"aadbbcbcac"`, return true.
> When s3 = `"aadbbbaccc"`, return false.

## Solution

分析题目可知，可以用类似合并排序的手段组合字符串，比如s3的前三个字符，aad就直接可以拼成，问题在于如果s1中的字符和s2中的字符相同时，则会产生分支。

- 动态规划，使用二维数组来保存中间结果，例如dp[i][j]，表示s1的前i个字符与s2的前j个字符是否可以组成s3的前i+j个字符。那么，递推公式如下：

`dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1])`

## Code

### Python

```python
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        dp = [[False for j in range(n+1)] for i in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[m][n]
```

### C++

```cpp

```