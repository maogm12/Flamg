# 007-Reverse Integer

## Problem

> Reverse digits of an integer.

> Example1: x = 123, return 321  
> Example2: x = -123, return -321

## Solution

这题主要要注意溢出和负数的处理，溢出返回 0

我们从低到高位取数，然后接到结果后面，同时判断是否溢出

> tips

> 判断溢出模板哦

> ```cpp
result > INT_MAX/10 || result == INT_MAX/10 && digit > INT_MAX%10
> ```

## Code

### C++

```cpp
class Solution {
public:
    int reverse(int x) {
        if (x == INT_MIN) {
            return 0;
        }
        int sign = x >= 0 ? 1 : -1;
        x = abs(x);
        
        int result = 0;
        while (x != 0) {
            int digit = x%10;
            if (result > INT_MAX/10 || result == INT_MAX/10 && digit > INT_MAX%10) {
                return 0;
            }
            result = result * 10 + digit;
            x /= 10;
        }
        
        return sign * result;
    }
};
```
