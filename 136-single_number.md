# 136-Single Number

## Problem

> Given an array of integers, every element appears twice except for one. Find that single one.

> Note:
>  Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

## Solution

- 哈希

    万能的哈希，何止是两次，任意次数都没问题。

- 位运算

    复习一下异或运算

    ```
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 1 = 0
1 ^ 0 = 1
    ```

    可见相同的数字异或运算之后变成了 `0`，任意数字与 `0` 异或还是这个数，我们可以把所有的数字做做异或操作，最后得到的结果就是要找的那个数

## Code

### Python

```python
import operator
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # in python3
        # import functools
        # return functools.reduce(operator.xor, A)
        return reduce(operator.xor, A)
```

### C++

```cpp
class Solution {
public:
    int singleNumber(int A[], int n) {
        return accumulate(A, A + n, 0, bit_xor<int>());
    }
};
```
