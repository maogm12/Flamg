# 060-Permutation Sequence

## Problem
> The set [1,2,3,…,n] contains a total of n! unique permutations.

> By listing and labeling all of the permutations in order,
 We get the following sequence (ie, for n = 3):

> ```
> 1."123"
> 2."132"
> 3."213"
> 4."231"
> 5."312"
> 6."321"
> ```

> Given n and k, return the kth permutation sequence.

> Note: Given n will be between 1 and 9 inclusive.

求第 `k` 个排列

## Solution

- 暴力算法

    还记得 `next_permutation` 不，只要我们执行 `k - 1`次，即可找到第 `k` 个解。

    不过这个时间复杂度略大啊，`next_permutation` 的复杂度为 O(n)，但是对于 `n` 个数，存在排列 `n!` 个。所以这个复杂度为 O(n*(n!))，超级大哦！

- 推算法之循环

    这种排列组合问题推演之！

    对于某一列数，求它从小到大所有的排列，我们在最高位依次放从小到大的数，剩下的数递归处理。所以总共排列的数目设为`L(n)`，我们可以得到一个关系：
    `L(n) = n * L(n)`，擦，这货不是阶乘么。

    其中从小到大有 `n` 段 `L(n)` 长度的排列。举个栗纸：

    ```
    对于 1,2,3 的组合，可以分成三组
    1 2 3
    1 3 2    第 0 组

    2 1 3
    2 3 1    第 1 组

    3 1 2
    3 2 1    第 2 组
    ```

    说这么多，其实我是想说，如果我们可以确定 `k` 在第几组，就可以确定第一个数字了，后面的处理流程类似，可以递归或者循环处理。

    比如上面的栗纸，后面的索引位置是基于零的。如果 `k = 4`，那么我们可以发现这个排列在上面的第 `2` 组里面。怎么算呢，`k / L(2) = 4 / 2`，然后我们知道第一个位置应该填第三大的数，就是 `1,2,3` 里面的 `3`。然后就是找第 `2` 组里面的第 `0 (= k % L(2))` 个排列，我们发现是第`0` 个子小组，所以第二个位置应该填剩下的数里面最小的数，就是 `1,2` 里面的 `1`。以此类推。

    所以我们可以先得到 `L` 的序列，然后循环计算按每一位应该填那个数字。

- 推算法之递归

    基于上面的推算，也可以使用递归去做。

## Code

### Python

```python
# blah blah
```

### C++

循环版本

```cpp
class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> digits;
        for (int i = 0; i < n; ++i) {
            digits.push_back(i + 1);
        }

        stringstream ss;
        if (k > 1) {
            --k;  // zero-based
            // 计算组的大小
            vector<int> groupSizes(1, 1);
            for (int i = 1; i < n - 1; ++i) {
                groupSizes.push_back(*(groupSizes.rbegin()) * (i + 1));
            }

            // 计算应该填什么数
            for (auto sizeIt = groupSizes.rbegin(); sizeIt != groupSizes.rend(); ++sizeIt) {
                auto it = digits.begin() + k / *sizeIt;
                k %= *sizeIt;
                ss << *it;
                digits.erase(it);  // 该数字已被使用，删掉这个数
            }
        }

        for (int i = 0; i < digits.size(); ++i) {
            ss << digits[i];
        }

        return ss.str();
    }
};
```
