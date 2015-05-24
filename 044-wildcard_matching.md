# 044-Wildcard Matching

## Problem

> Implement wildcard pattern matching with support for '?' and '*'.

> ```
> '?' Matches any single character.
> '*' Matches any sequence of characters (including the empty sequence).

> The matching should cover the entire input string (not partial).

> The function prototype should be:
> bool isMatch(const char *s, const char *p)

> Some examples:
> isMatch("aa","a") → false
> isMatch("aa","aa") → true
> isMatch("aaa","aa") → false
> isMatch("aa", "*") → true
> isMatch("aa", "a*") → true
> isMatch("ab", "?*") → true
> ```

## Solution

- DP

    - 最优子结构

    假设我们要判断 s[0...n] / p[0...m] 是否匹配，我们判断最后一个字符：
        1. 最后一个字符相等（包括'?'），我们要判断 s[0...n-1] / p[0...m-1]
        2. p[m] == '*'，我们要判断 s[0...n-1] / p[0...m] 或者 s[0...n-1] / p[0...m-1]
        3. false

    你看，最优子结构就出来了吧

    - 重叠子问题

    明显有啊

    所以可以用DP破之

- 


## Code

### Python

```python
# blahblah
```

### C++

DP，可惜leetcode上有一个超级大的测试用例。sizeS * sizeP 接近 1G 内存，所以这在leetcode上是过不去的。。。

```cpp
bool isMatch(string s, string p) {
    int sizeS = s.size(),
        sizeP = p.size();
    bool matched[sizeS + 1][sizeP + 1];
    memset(matched, false, sizeof(matched));
    matched[0][0] = true;
    for (int i = 1; i <= sizeS; ++i) {
        matched[i][0] = false;
    }
    for (int i = 1; i <= sizeP; ++i) {
        matched[0][i] = matched[0][i - 1] && p[i - 1] == '*';
    }

    for (int i = 1; i <= sizeS; ++i) {
        for (int j = 1; j < sizeP; ++j) {
            if (s[i - 1] == p[j - 1] || p[j - 1] == '?') {
                matched[i][j] = matched[i - 1][j - 1];
            } else if (p[j - 1] == '*') {
                matched[i][j] = matched[i][j - 1] || matched[i - 1][j];
            } else {
                matched[i][j] = false;
            }
        }
    }

    return matched[sizeS][sizeP];
}
```
