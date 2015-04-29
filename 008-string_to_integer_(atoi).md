# 008-String to Integer (atoi)

## Problem

> Implement atoi to convert a string to an integer.

> Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

> Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

字符串转整数

## Solution

这题坑很多，有很多异常情况

1. 空串，应该返回 `0`
2. 前置的空字符，应该忽略
3. 注意符号！！！`+/-`
4. 中间遇到异常字符，那么连同后面的所有东西一起丢弃
5. 异常情况应该返回 `0`
6. 溢出处理！！！正数返回 `INT_MAX`，负数应该返回 `INT_MIN`

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int myAtoi(string str) {
        int size = str.size();
        int result = 0;
        int i = 0;
        int sign = 1;
        bool overflow = false;

        // leading space
        while (i < size && isspace(str[i])) ++i;

        // detect sign
        if (i < size) {
            if (str[i] == '-') {
                sign = -1;
                ++i;
            } else if (str[i] == '+') {
                ++i;
            }
        }

        // OK, something like '-  123' is not allowed
        // while (i < size && isspace(str[i])) ++i;

        // digits
        int threshold = INT_MAX / 10;
        while (i < size) {
            if (!isdigit(str[i])) {
                break;
            }

            int digit = str[i] - '0';
            // detect overflow
            if (result > threshold || result == threshold && digit >= 8) {
                overflow = true;
                break;
            } else {
                result = result * 10 + digit;
                ++i;
            }
        }

        if (overflow) {
            return sign == 1 ? INT_MAX : INT_MIN;
        }
        return sign * result;
    }
};
```
