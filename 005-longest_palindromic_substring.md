# 005-Longest Palindromic Substring

## Problem

> Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

	找字符串中的最长回文子串

## Solution

- 暴力算法。对字符串的每个字符进行两边扩展操作，找出以该字符为中心的最长回文字符串。当然，考虑奇数和偶数的情况下，还需要对每两个相邻字符进行判断。
- 优化算法。正所谓先用暴力得初解，再据题意破玄奇。

	首先，定义一个概念，`最大半回文长度`:即对奇数长度的回文串，其以中心为起点，以一段为端点的字符串长度。

	考虑回文字符串的性质。如这个字符串`abacabadfeg`，只考虑奇数情况，以每个字符为中心的最大半回文长度分别为`12141211111`。可以看到，前7个字符是回文字符串，但是前7个的最大半回文长度也是基于第4个数对称的。
	
	当然，也有其他情况，比如`abacababfeg`，它的最长半回文长度分别为`12141221111`，注意第7个位置，与第一个示例不同。
	
	所以，对于一个字符来说，如果之前的回文子串所覆盖的范围已经包含到它，那么，可以利用回文串的性质来初始化它的最大半回文长度，然后再向两边判断字符是否相等。
	
> 对于一个字符串来说，如果要同时考虑奇数和偶数的情况，可以使用一个trick，即在每两个字符中间插入一个其他字符，如#。即abac变为#a#b#a#c#，这样，偶数情况也变成了奇数情况。
	

## Code

### Python

```python
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        s = '#' + '#'.join(s) + '#'
        mx = 0
        id = 0
        len_s = len(s)
        p = [0 for i in range(len_s)]
        i = 0
        while i < len_s:
            if mx > i:
                p[i] = min(p[2*id-i], mx - i)
            else:
                p[i] = 1
            while i-p[i] >= 0 and i+p[i] < len_s and s[i-p[i]] == s[i+p[i]]:
                p[i] += 1
            if mx < p[i] + i:
                mx = p[i] + i
                id = i
            i += 1
        i = 0
        max_value = 0
        max_index = -1
        while i < len_s:
            if p[i] > max_value:
                max_value = p[i]
                max_index = i
            i += 1
        result = s[max_index - max_value + 1: max_index + max_value]
        return result.replace('#', '')
```

### C++

```cpp

```