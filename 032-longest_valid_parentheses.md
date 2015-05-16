# 032-Longest Valid Parentheses

## Problem

> Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

> For `"(()"`, the longest valid parentheses substring is `"()"`, which has length = 2.

> Another example is `")()())"`, where the longest valid parentheses substring is `"()()"`, which has length = 4.

## Solution

使用一个栈保存状态，使用一个数组来保存以当前字符为结尾的最长合法括号对的长度。
如`()((()))`，它的最长合法括号对数组为[0,2,0,0,0,2,4,8]

以最后一个右括号为例，它和第三个字符匹配为一个括号对，他们之间的长度为6，而之前的两个也是一个合法对，所以加上之前的长度2，得到最后的长度8。


## Code

### Python

```python
class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = []
        len_s = len(s)
        if len_s == 0:
            return 0
        dp = [0 for i in range(len_s)]
        max_length = 0
        for i in range(len_s):
            if s[i] == '(':
                stack.append((i))
            else:
                if len(stack) != 0:
                    c_i = stack.pop()
                    dp[i] = i - c_i + 1
                    if c_i > 0:
                        dp[i] += dp[c_i - 1]
                    max_length = max(dp[i], max_length)
        return max_length
```

### C++

```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        int len_s = s.length();
        if (len_s == 0) {
            return 0;
        }
        vector<int> dp(len_s, 0);
        stack<int> index_stack;
        int max_length = 0;
        for (int i = 0; i < len_s; i++) {
            if (s[i] == '(') {
                index_stack.push(i);
            } else {
                if (!index_stack.empty()) {
                    int c_index = index_stack.top();
                    index_stack.pop();
                    dp[i] = i - c_index + 1;
                    if (c_index > 0) {
                        dp[i] += dp[c_index-1];
                    }
                    max_length = max(max_length, dp[i]);
                }
            }
        }
        return max_length;
    }
};
```