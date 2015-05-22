# 041-First Missing Positive

## Problem

> Given an unsorted integer array, find the first missing positive integer.

> For example,  
> Given `[1,2,0]` return `3`,  
> and `[3,4,-1,1]` return `2`.

> Your algorithm should run in O(n) time and uses constant space.

## Solution

- 排序法

    排序，然后从前往后找，找到第一个缺失的正数

    寻找缺失这个过程复杂度为 O(n)，所以整个算法短板在排序，一般来说复杂度在 O(nlogn)，空间复杂度 O(1)

- 哈希法

    我们用哈希保存出现过的数字，然后遍历整数，知道某个数不在哈希表里面为止

    时间复杂度为 O(n)，空间复杂度为 O(n)

- **排序法

    我不知道这个方法叫啥名字。。。

    因为我们要找第一个缺失的正数，我们把 1 放到第 0 个位置，2 放到第 1 个位置...

    就是说 n 该放到 n - 1 这个位置上，怎么放，交换呗。

    遍历一遍数组，把每个数放到该放的位置上，这样结果就是前面一截变成了 1,2,3,4,5...这个有序排列，
    这样就很简单的能找出哪儿丢数了

## Code

### Python

```python

```

### C++

```cpp
int firstMissingPositive(vector<int>& nums) {
    if (nums.empty()) {
        return 1;
    }

    for (int i = 0; i < nums.size(); ++i) {
        // 把这个位置上换成该放的数
        while (nums[i] != i + 1) {
            // 负数就不用管了
            // 比数组长度大的数也不用管了，这货前面肯定有缺失的
            // 或者要交换的数相同，那换个毛
            if (nums[i] <= 0 || nums[i] > nums.size() || nums[i] == nums[nums[i] - 1]) {
                break;
            }

            // 把这个数扔到该放的位置上
            swap(nums[i], nums[nums[i] - 1]);
        }
    }

    for (int i = 0; i < nums.size(); ++i) {
        if (nums[i] != i + 1) {
            return i + 1;
        }
    }

    return nums.size() + 1;
}
```
