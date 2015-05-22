# 043-Multiply Strings

## Problem

> Given two numbers represented as strings, return multiplication of the numbers as a string.

> Note: The numbers can be arbitrarily large and are non-negative.

## Solution

- 模拟法

    模拟竖式运算

## Code

### Python

```python

```

### C++

```cpp
string multiply(string num1, string num2) {
    if (num1.empty() || num2.empty()) {
        return "";
    }

    string result = multiply(num1, num2[num2.size() - 1] - '0');
    for (int i = 1; i < num2.size(); ++i) {
        string rh = multiply(num1, num2[num2.size() - 1 - i] - '0');
        result = add(result, rh, i);
    }
    reverse(result.begin(), result.end());

    // 去除前置的 0 ！！！
    for (int i = 0; i < result.size(); ++i) {
        if (result[i] != '0') {
            return result.substr(i);
        }
    }
    return "0";
}

// 字符串和一个数字相乘
string multiply(string num, int digit) {
    stringstream result;
    int carry = 0;
    for (int i = num.size() - 1; i >= 0; --i) {
        carry += digit * (num[i] - '0');
        result << carry % 10;
        carry /= 10;
    }
    if (carry > 0) {
        result << carry;
    }

    return result.str();
}

// 数字相加，数字是倒着存的，然后有一个偏移，模拟竖式里面那个
string add(string& rn1, string& rn2, int offset) {
    stringstream result;
    for (int i = 0; i < offset; ++i) {
        if (i < rn1.size()) {
            result << rn1[i];
        } else {
            result << 0;
        }
    }

    int carry = 0;
    for (int i = 0; i < rn2.size(); ++i) {
        if (i + offset < rn1.size()) {
            carry += rn1[i + offset] - '0';
        }
        carry += rn2[i] - '0';
        result << carry % 10;
        carry /= 10;
    }
    if (carry > 0) {
        result << carry;
    }

    return result.str();
}
```
