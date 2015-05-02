# 115-Distinct Subsequences

## Problem

> Given a string S and a string T, count the number of distinct subsequences of T in S.

> A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

> Here is an example:
S = "rabbbit", T = "rabbit"

> Return 3.

## Solution

- A解法：假设f(i,j)为t的前i个字符与s的前j个字符的不同子串数目，那么可得到递推关系：

	`f(i,j) = f(i,j-1) if s[j] != t[i]`
	`f(i,j) = f(i,j-1) + f(i-1,j-1) if s[j] == t[i]`

- B解法：当然，还可以采取另外一种假设方式，将坐标互换，即f(i,j)为s的前i个字符与t的前j个字符的不同子串数目，那么递推关系变为：
	
	`f(i,j) = f(i-1,j) if s[i] != t[j]`
	`f(i,j) = f(i-1,j) + f(i-1,j-1) if s[i] == t[j]`
	
- 分析
	
	解法A和解法B利用到的信息都是当前层和上一层的，因而可以使用滚动数组的方式进行这样的动规方法的内存压缩。即使用两个数组分别保存当前层和上一层的信息。
	但是解法A利用的信息是当前层和上一层的，而解法B利用的信息则全是上一层的，因而，使用滚动数组的方式进行压缩时，解法B能只依靠一个数组。而解法A则仍需要两个数组。
	

## Code

### Python

```optimized on memory python for B
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        len_s = len(s)
        len_t = len(t)
        dp = [0 for j in range(len_t+1)]
        dp[0] = 1
        for i in range(1, len_s+1):
            j = len_t
            while j >= 1:
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]
                j -= 1
        return dp[len_t]
```

### C++

```cpp for A
class Solution {
public:
    int numDistinct(string s, string t) {
        int len_s = s.length();
        int len_t = t.length();
        int dp[len_t+1][len_s+1];
        
        for (int j = 0; j <= len_s; j++) {
            dp[0][j] = 1;
        }
        
        for (int i = 1; i <= len_t; i++) {
            dp[i][0] = 0;
            for (int j = 1; j <= len_s; j++) {
                dp[i][j] = dp[i][j-1];
                if (t[i-1] == s[j-1]) {
                    dp[i][j] += dp[i-1][j-1];
                }
            }
        }
        return dp[len_t][len_s];
    }
};
```

```cpp for B
class Solution {
public:
    int numDistinct(string s, string t) {
        int len_s = s.length();
        int len_t = t.length();
        int dp[len_s+1][len_t+1];
        
        dp[0][0] = 1;
        for (int j = 1; j <= len_t; j++) {
            dp[0][j] = 0;
        }
        for (int i = 1; i <= len_s; i++) {
            dp[i][0] = 1;
            for (int j = 1; j <= len_t; j++) {
                dp[i][j] = dp[i-1][j];
                if (s[i-1] == t[j-1]) {
                    dp[i][j] += dp[i-1][j-1];
                }
            }
        }
        return dp[len_s][len_t];
    }
};
```

```optimized on memory cpp for B
class Solution {
public:
    int numDistinct(string s, string t) {
        int len_s = s.length();
        int len_t = t.length();
        int dp[len_t+1];
        
        dp[0] = 1;
        for (int j = 1; j <= len_t; j++) {
            dp[j] = 0;
        }
        for (int i = 1; i <= len_s; i++) {
            for (int j = len_t; j >= 1; j--) {
                if (s[i-1] == t[j-1]) {
                    dp[j] += dp[j-1];
                }
            }
        }
        return dp[len_t];
    }
};
```