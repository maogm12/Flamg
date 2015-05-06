# 014-Longest Common Prefix

## Problem

> Write a function to find the longest common prefix string amongst an array of strings.

## Solution

- 纵向扫描

    关键是确定这个公共前缀的长度，所以我们从零开始，每次都纵向扫描。
    如果碰到某个字符串结束，或者相邻的两个字符串对应的字符不相等，
    前缀查找就此打住了

## Code

### Python

```python
# 
```

### C++

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) {
            return "";
        }

        int i = 0;
        int size = strs.size();
        if (size == 1) {
            return strs[0];
        }

        while (true) {
            for (int j = 0; j < size - 1; ++j) {
                if (i == strs[j].size() || i == strs[j + 1].size() || strs[j][i] != strs[j + 1][i]) {
                    return strs[j].substr(0, i);
                }
            }

            ++i;
        }
    }
};
```
