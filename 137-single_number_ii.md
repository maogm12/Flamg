# 137-Single Number II

## Problem

> Given an array of integers, every element appears three times except for one. Find that single one.

> Note:

>  Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

一个数组里除了某个数之外所有的数都出现过 3 次，找出这个数

## Solution

- 哈希法

    我们记录每一个数出现的次数，然后看哪个数字只出现了一次

    时间复杂度 O(n)，空间复杂度 O(n)

- 计算每一位出现次数法

    这个方法很神奇啊！可以推广到算任意次

    因为数组里面都是整数，我们开辟一个 `sizeof(int) * 8` 的数组，把每一个数的对应的位相加，也就是统计的是每一位出现 `1` 的次数。

    - 若一个数出现了 3 次，对应的位上的数字会增加 3
    - 若某个数只出现 1 次，对应的位上的数字只会增加 1

    所以最后，我们对 3 求模，就可以得到那个只出现 1 次的数的二进制表示。

    这样这个数出现了两次也是可以找出来的耶

    时间复杂度为 O(n)，空间复杂度为一个固定长度的数组，所以是 O(1)

## Code

### Python

```python

```

### C++

hash 版本

```cpp
class Solution {
public:
    int singleNumber(int A[], int n) {
        unordered_map<int, int> times;
        for (int i = 0; i < n; ++i) {
            if (times.find(A[i]) == times.end()) {
                times[A[i]] = 1;
            } else {
                times[A[i]] += 1;
            }
        }

        for (auto pair: times) {
            if (pair.second == 1) {
                return pair.first;
            }
        }
    }
};
```

计算每一位出现次数法

```cpp
class Solution {
public:
    int singleNumber(int A[], int n) {
        const int digits = sizeof(int) * 8;
        int count[digits];
        fill_n(count, digits, 0);
        for (int i = 0; i < n; ++i) {
            int num = A[i];
            for (int j = 0; j < digits; ++j) {
                count[j] += num & 1;
                num >>= 1;
            }
        }

        int result = count[digits - 1] % 3;
        for (int i = digits - 2; i >= 0; --i) {
            count[i] = count[i] % 3;
            result = result << 1 | count[i];
        }

        return result;
    }
};
```
