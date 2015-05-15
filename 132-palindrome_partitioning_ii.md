# 132-Palindrome Partitioning II

## Problem

> Given a string s, partition s such that every substring of the partition is a palindrome.

> Return the minimum cuts needed for a palindrome partitioning of s.

> For example, given s = `"aab"`,

> Return 1 since the palindrome partitioning `["aa","b"]` could be produced using 1 cut.

## Solution

- 动态规划，假设字符串长度为n，那么保存一个同样长度的数组，设为dp，dp[i]表示字符串从0到i(表示为s[0...i])的最小cut数。那么，可以分情况处理，
	- `dp[i] = 0` if `s[0...i]` 回文
	- `dp[i] = min(dp[j-1] + 1) ` for all j 满足 `s[j...i]` 回文
	
	那么，如何快速的求解s[j...i]是否回文？可以利用回文串的性质，即：
	- is_palindrome(s[j...i]) == true 
	- is_palindrome(s[j+1...i-1]) == true and s[j] == s[i]
	
	所以，根据此性质，我们可以在O(n<sup>2</sup>)时间内求出所有子串是否回文。
	 
## Code

### Python

```python
class Solution:
    # @param s, a string
    # @return a list of lists of string
	def minCut(self, s):
		len_s = len(s)
		
		# 求解所有子串是否回文
		dp = [ [0 for j in range(len_s)] for i in range(len_s)]
		i = 0
		while i < len_s:
			left = i
			right = i
			while left >= 0 and right < len_s:
				if s[left] == s[right]:
					dp[left][right] = 1
				else:
					break
				left -= 1
				right += 1
			left = i-1
			right = i
			while left >= 0 and right < len_s:
				if s[left] == s[right]:
					dp[left][right] = 1
				else:
					break
				left -= 1
				right += 1
			i += 1
		
		# 求解最小cut数目
		dp_value = [0 for i in range(len_s)]
		i = 1
		while i < len_s:
			if dp[0][i] == 1:
				dp_value[i] = 0
			else:
				j = i-1
				dp_value[i] = dp_value[j] + 1
				while j >= 0:
					if dp[j+1][i] == 1:
						if dp_value[j] + 1 < dp_value[i]:
							dp_value[i] = dp_value[j] + 1
					j -= 1
			i += 1
		return dp_value[-1]

```

### C++

```cpp
class Solution {
public:
    int minCut(string s) {
        int len_s = s.length();
        vector<vector<bool> > dp(len_s, vector<bool>(len_s, false));
        int i = 0;
        while (i < len_s) {
            palindrome(s, dp, i, i, len_s);
            palindrome(s, dp, i-1, i, len_s);
            i++; 
        }
        vector<int> dp_value(len_s, 0);
        i = 1;
        while (i < len_s) {
            if (!dp[0][i]) {
                dp_value[i] = dp_value[i-1] + 1;
                for (int j = 1; j < i; j++) {
                    if (dp[j][i]) {
                        dp_value[i] = min(dp_value[j-1]+1, dp_value[i]);
                    }
                }
            }
            i++;
        }
        return dp_value[len_s-1];
    }
    
    void palindrome(string &s, vector<vector<bool> > &dp, int left, int right, int len_s) {
        while (left >= 0 && right < len_s) {
            if (s[left] == s[right]) {
                dp[left--][right++] = true;
            } else {
                return;
            }
        }
    }
};
```