# 010-Regular Expression Matching

## Problem

> Implement regular expression matching with support for '.' and '*'.

> ```
> '.' Matches any single character.
> '*' Matches zero or more of the preceding element.

> The matching should cover the entire input string (not partial).

> The function prototype should be:
> bool isMatch(const char *s, const char *p)

> Some examples:
> isMatch("aa","a") → false
> isMatch("aa","aa") → true
> isMatch("aaa","aa") → false
> isMatch("aa", "a*") → true
> isMatch("aa", ".*") → true
> isMatch("ab", ".*") → true
> isMatch("aab", "c*a*b") → true
> ```

## Solution

这个题很坑哈

首先读懂题，鄙人两次做题两次都弄错了题意。。。

> `'.'` 匹配一个字符  
> `'*'` 匹配一个或者多个前一个字符

这个问题是一个典型的动态规划题，我们先来找转移方程

定 `f(ps,pp)` 为字符串下标 `ps` 以前的字串和模板下标 `pp` 以前的字串的匹配情况，例如

```
aab
 ^     ps = 1
c*a*b
    ^  pp = 4
```

例如这里字串 `a` 和子模板串 `c*a*` 是匹配的，即`f(1,4) = true`

然后确定转义方程，对于模板串的三种情况

1. 下标前面的字符是 `.`，匹配一个字符

    `f(ps,pp) = f(ps - 1, pp - 1)`

2. 下标前的字符为 `*`，匹配 0 个或多个字符

    `f(ps,pp) = f(ps, pp - 2) || f(ps - 1, pp)`

3. 下标前的字符为普通字符，匹配失败或一个字符

    `f(ps,pp) = false` 或
    `f(ps,pp) = f(ps - 1, pp - 1)`

然后我们用迭代法可破之！

## Code

### Python

```python
# 累死我了
```

### C++

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int sizeS = s.size(), sizeP = p.size();

        // 记录中间状态
        bool matched[sizeS + 1][sizeP + 1];
        matched[0][0] = true;
        for (int i = 1; i < sizeS + 1; ++i) {
            matched[i][0] = false;
        }

        for (int i = 1; i < sizeP + 1; ++i) {
            for (int j = 0 ; j < sizeS + 1; ++j) {
                if (p[i - 1] == '.') {
                    matched[j][i] = j == 0 ? false : matched[j - 1][i - 1];
                } else if (p[i - 1] == '*') {
                    if (j == 0 || p[i - 2] != '.' && p[i - 2] != s[j - 1]) {
                        matched[j][i] = matched[j][i - 2];
                    } else {
                        matched[j][i] = matched[j][i - 2] || matched[j - 1][i];
                    }
                } else {
                    if (j == 0 || p[i - 1] != s[j - 1]) {
                        matched[j][i] = false;
                    } else {
                        matched[j][i] = matched[j - 1][i - 1];
                    }
                }
            }
        }

        return matched[sizeS][sizeP];
    }
};
```
