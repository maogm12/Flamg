# 072-Edit Distance

## Problem

> Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

> You have the following 3 operations permitted on a word:
> 
- Insert a character
- Delete a character
- Replace a character

## Solution

对于两个字符串s1和s2，假设s1的前i个字符和s2的前j个字符的编辑距离为f[i][j]，那么根据编辑距离的定义，可以得到如下规律：

`f[i][j] = f[i-1][j-1] if s1[i] == s2[j]`
`f[i][j] = min(f[i-1][j], f[i-1][j-1], f[i][j-1]) + 1`

其中，第二步中的min函数内的三个值分别代表s1增加一个字符，s1/s2替换一个字符，s2增加一个字符。

## Code

### Python

```python
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0 for j in range(len2+1)] for i in range(len1+1)]
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[len1][len2]
```

### C++

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        int dp[len1+1][len2+1];
        for (int i = 0; i <= len1; i++) {
            for (int j = 0; j <= len2; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = max(i,j);
                } else if (word1[i-1] == word2[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1;
                }
            }
        }
        return dp[len1][len2];
    }
};
```