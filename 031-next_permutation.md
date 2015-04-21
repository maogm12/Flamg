# 031-Next Permutation

## Problem

> Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
>
> If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
>
> The replacement must be in-place, do not allocate extra memory.
>
> Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
> ```
> 1,2,3 → 1,3,2
> 3,2,1 → 1,2,3
> 1,1,5 → 1,5,1
> ```

找到下一个排列。

## Solution

- STL

    恩，用C++可以作弊，标准库自带 `next_pemutation` 函数

- Manually

    如果一列数已经是逆序的了，那么这个排列已经是最大的了，所以，
    只要存在一个数比后面的数小，那么依然可以排一个更大的排列出来。

    - 首先找到这个数
    - 然后我们起码把这个位置换一个大一点的数，换哪一个呢？
    应该是后面那些数里面比这个数刚好大一点的数，用 `upper_bound` 即可。
    - 然后后面这些数应该要从小往大排列才行

    看代码

## Code

### Python

```python
# wait a minute
```

### C++ with STL

```cpp
class Solution {
public:
    void nextPermutation(vector<int> &num) {
        next_permutation(num.begin(), num.end());
    }
};
```

### C++
```cpp
class Solution {
public:
    void nextPermutation(vector<int> &num) {
        if (num.size() <= 1) {
            return;
        }

        auto last = num.rbegin();
        auto swapPos = last + 1;
        while (swapPos != num.rend() && *swapPos >= *(swapPos - 1)) {
            ++swapPos;
        }

        if (swapPos != num.rend()) {
            auto toSwap = upper_bound(num.rbegin(), swapPos - 1, *swapPos);
            iter_swap(swapPos, toSwap);
        }

        // 后面本来是逆序，反转就可以了
        reverse(num.rbegin(), swapPos);
    }
};
```
