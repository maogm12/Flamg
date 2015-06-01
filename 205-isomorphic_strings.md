# 205-Isomorphic Strings

## Problem

> Given two strings s and t, determine if they are isomorphic.

> Two strings are isomorphic if the characters in s can be replaced to get t.

> All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

> For example,
> 
> Given "egg", "add", return true.

> Given "foo", "bar", return false.

> Given "paper", "title", return true.

## Solution

没有两个字母影响到相同的字母，一个字母也不会映射到不同的字母上。所以保存两个映射字典，当违反映射字典时，返回false。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int len_s = s.length();
        int len_t = t.length();
        if (len_s != len_t) {
            return false;
        }
        unordered_map<char, char> from;
        unordered_map<char, char> to;
        for (int i = 0; i < len_s; i++) {
            auto from_it = from.find(s[i]);
            auto to_it   = to.find(t[i]);
            if (from_it != from.end() && to_it != to.end()) {
                if (from[s[i]] == t[i] && to[t[i]] == s[i]) {
                    continue;
                } else {
                    return false;
                }
            } else if (from_it == from.end() && to_it == to.end()) {
                from.insert(make_pair(s[i], t[i]));
                to.insert(make_pair(t[i], s[i]));
            } else {
                return false;
            }
        }
        return true;
    }
};
```