# 067-Add Binary

## Problem

> Given two binary strings, return their sum (also a binary string).
>
> For example,
>
> a = `"11"`  
> b = `"1"`  
> Return `"100"`.

模拟二进制加法

## Solution

- 模拟竖式

无论是多少进制的加法用竖式模拟起来都是一样的，算当前为的和，然后进位

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        int sizeA = a.size(),
            sizeB = b.size(),
            resultSize = max(sizeA, sizeB) + 1;
        string result(resultSize, '0');  // 分配空间
        int carry = 0;  // 进位信息
        for (int i = 1; i <= resultSize; ++i) {
            if (sizeA - i >= 0) {
                carry += a[sizeA - i] - '0';
            }

            if (sizeB - i >= 0) {
                carry += b[sizeB - i] - '0';
            }

            // 通用模板
            // current = carry % base
            // carry /= base
            result[resultSize - i] = carry % 2 + '0';
            carry /= 2;
        }
        if (!result.empty() && result[0] == '0') {
            result = result.substr(1);
        }

        return result;
    }
};
```
