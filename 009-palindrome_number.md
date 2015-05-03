# 009-Palindrome Number

## Problem

> Determine whether an integer is a palindrome. Do this without extra space.

判断一个数字是否是回文字符串

## Solution

- 作弊法

    把数字转成字符串然后判断是否为回文串 ==

- 数学法

    Let's do some math.

    首先我们如果要判断回文的话要知道最高位和最低位。求最低位简单，`%10` 即可，
    求最高位的话，首先我们得知道有多少位(`n`)，然后除以 `10^n`。所以关键在于如何求这个数的位数，那么就循环判断之。

## Code

### Python

做个弊，表学我

```python
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
```

### C++

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        // 负数负分滚粗
        if (x < 0) {
            return false;
        }

        // 求除数，其实就是另一个形式的位数
        int divider = 1;
        // 千万不要尼玛用 >0，最后再 /10，因为会溢出啊 TT
        while (x / divider >= 10) {
            divider *= 10;
        }

        while (divider > 1) {
            int high = x / divider;
            int low = x % 10;
            if (high != low) {
                return false;
            }
            x %= divider;
            x /= 10;
            divider /= 100;
        }

        return true;
    }
};
```
