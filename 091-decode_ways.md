# 091-Decode Ways

## Problem

> A message containing letters from A-Z is being encoded to numbers using the following mapping:
>
```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```
Given an encoded message containing digits, determine the total number of ways to decode it.

> For example,
Given encoded message `"12"`, it could be decoded as `"AB"` (1 2) or `"L"` (12).

> The number of ways decoding `"12"` is 2.

## Solution

根据题意描述，对于一个字符串s，假设`f(i)`是s的前i个字符的解码方式数目。那么有递推式

`f(i) = f(i-1) + f(i-2)  if 1 <= int(s[i]) <= 9 and 10 <= int(s[i-1]s[i]) <= 26`
`f(i) = f(i-2) if int(s[i]) == 0 and 10 <= int(s[i-1]s[i]) <= 26`

即，

- 当当前字符在1-9范围内且前一位与当前位字符组成的两位数在10-26内时，则可以以这两种方法分别解码。
- 当当前字符为0且前一位与当前字符组成的两位数在10-26内时，则只能以两位数的方式来解码。

## Code

### Python

```python
class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        len_s = len(s)
        if len_s == 0 or s[0] == '0':
            return 0
        dp = [0 for i in range(len_s)]
        dp[0] = 1
        for i in range(1, len_s):
            if 1 <= int(s[i:i+1]) <= 9:
                dp[i] = dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i < 2:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[len_s-1]
```

### C++

```cpp
class Solution {
public:
    int numDecodings(string s) {
        int len_s = s.length();
        if (len_s == 0 || s[0] == '0') {
            return 0;
        }
        int dp[len_s];
        dp[0] = 1;
        for (int i = 1; i < len_s; i++) {
            if ( s[i] >= '1' && s[i] <= '9' ) {
                dp[i] = dp[i-1];
            } else {
                dp[i] = 0;
            }
            if (s[i-1] == '1' || (s[i-1] == '2' && s[i] <= '6')) {
                if (i < 2) {
                    dp[i] += 1;
                } else {
                    dp[i] += dp[i-2];
                }
            }
        }
        return dp[len_s-1];
    }
};
```