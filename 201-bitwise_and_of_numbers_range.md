# 201-Bitwise AND of Numbers Range

## Problem

> Given a range [m, n] where `0 <= m <= n <= 2147483647`, return the bitwise AND of all numbers in this range, inclusive.

> For example, given the range `[5, 7]`, you should return 4.

## Solution

- 暴力算法：一个一个的搞起
- 简单算法：因为是区间的上限和下限，考虑下限值逐步加1的情况，如5，6，7

```
5      = 101
6      = 110
7      = 111
result = 100
```

所以，将上限和下限两个数转化成二进制，从高位往低位遍历，当两个位不同时，则该位后面的位都为0

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int result = 0;
        for (int i = 31; i >= 0; i--) {
            bool m_i = ((1 << i) & m) > 0;
            bool n_i = ((1 << i) & n) > 0;
            if (m_i == n_i) {
                if (m_i && n_i) {
                    result += 1 << i;
                }
            } else {
                break;
            }
        }
        return result;
    }
};
```