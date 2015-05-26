# 058-Length of Last Word

## Problem

> Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

> If the last word does not exist, return 0.

> Note: A word is defined as a character sequence consists of non-space characters only.

> For example,
Given s = "Hello World",
return 5.

## Solution

首先，去掉末尾的空格，然后再向前找空格。 比如`"hello world  "`，先将后面的空格忽略不计，再找hello和world之间的空格。

## Code

### Python

```python
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        len_s = len(s)
        j = len_s - 1
        while j >= 0:
            if s[j] == ' ':
                len_s -= 1
                j -= 1
            else:
                break
        while j >= 0:
            if s[j] == ' ':
                break
            j -= 1
        return len_s - j - 1
```

### C++

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int len_s = s.length();
        int j = len_s - 1;
        while (j >= 0) {
            if (s[j] == ' ') {
                len_s--;
                j--;
            } else {
                break;
            }
        }
        while (j >= 0) {
            if (s[j] == ' ') {
                break;
            }
            j--;
        }
        return len_s - j - 1;
    }
};
```

tidy the code

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1;
        while (i >= 0 && s[i] == ' ') --i;
        int len = 0;
        while (i >= 0 && s[i] != ' ') {
            ++len;
            --i;
        }
        return len;
    }
};
```
