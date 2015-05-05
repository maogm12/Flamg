# 028-Implement strStr()

## Problem

> Implement strStr().

> Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

实现字符串匹配算法，就是求子字符串在另一个字符串中第一次出现的位置

## Solution

- 暴力算法

    暴力算法最容易想，遍历字符串，从每一个位置开始匹配子串，如果匹配成功即可返回，失败则前功尽弃，从下一个位置重新开始

    时间复杂度是O(nk)，`n` 是字符串长度，`k` 是字串长度

- KMP 算法（Knuth–Morris–Pratt）

    牛逼闪闪的 KMP 算法出现了，主要是为了减少不必要的回溯。举个荔枝：

    ```
  ABDCEFABC
  ABC
    ^
  ABDCEFABC
   ABC
    ```

    当我们匹配到 `C` 的时候发现不匹配了，暴力算法及我们把字串往后移动一位，然后重新匹配，但是这里必然匹配失败，为什么，因为我们已经上一步匹配的时候看到字符串第二个字母 `B`（我们马上就要开始匹配的字母）等于字串的第二个字母，但是第一个字母和第二个字母明显不一样好伐！！！所以我们可以不匹配这一步，字串直接往后移。并且这个往后移动的长度可以通过分析字串得出。

    But,how? KMP 就可以来救场，我不会 ==


- BM 算法（Boyer-Moore）

    传说中 BM 算法平均效率比 KMP 快 3-5 倍，但是这个对输入串有要求。

    我也不会，大伙自己看书去。

- Sunday 算法

    发现一个 NB 算法，超级容易理解，为了在匹配失败时多往后跳，我们往前看一个字符，如果这个字符不在子串里，我们可以一举跳到后面开始，如果这个字符在字串里面，我们移动字串，使得这个字符与字串中出现位置对其，然后从头开始搜索。看个栗子就懂了：

    ```
  ABCDEFABG
  ABG
      ABG
        ABG
    ```

    对于这种情况，第一次匹配失败，后面（匹配整个字串长度之后的下一个）那个字符是 `D`，不在字串 `ABG` 中，所以我们可以跳过 `D` 直接从 `E` 开始搜索。

    然后发现又匹配失败，这次后面的字符是第二个 `B`，字串里面有 `B`，我们移动子字符串到两个 `B` 对其，然后搜索，成功！

## Code

### Python

得益于 Python 强大的 `for`，代码可以简单一点

```python
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        haystackSize = len(haystack)
        needleSize = len(needle)
        for i in xrange(haystackSize - needleSize + 1):
            for j in xrange(needleSize):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
```

### C++

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int haystackSize = haystack.size(),
            needleSize = needle.size();
        for (int i = 0; i <= haystackSize - needleSize; ++i) {
            bool isSubString = true;
            for (int j = 0; j < needleSize; ++j) {
                if (haystack[i + j] != needle[j]) {
                    isSubString = false;
                    break;
                }
            }

            if (isSubString) {
                return i;
            }
        }

        return -1;
    }
};
```

Sunday 算法

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int haystackSize = haystack.size(),
            needleSize = needle.size();
        unordered_map<char, int> lut;

        // calculate lut
        // 如果是 ASCII 字符，可以用数组模拟，比 map 快
        for (int i = 0; i < needleSize; ++i) {
            lut[needle[i]] = needleSize - i;
        }

        int i = 0;
        while (i <= haystackSize - needleSize) {
            int jump = 1, j = 0;
            while (j < needleSize) {
                if (haystack[i + j] != needle[j]) {
                    if (i + needleSize == haystackSize) {
                        return -1;
                    }

                    // 下一个字符
                    char later = haystack[i + needleSize];
                    jump = lut.find(later) == lut.end() ? needleSize : lut[later];
                    break;
                }
                ++j;
            }

            if (j == needleSize) {
                return i;
            }
            i += jump;
        }

        return -1;
    }
};
```
