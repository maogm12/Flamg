# 033-Search in Rotated Sorted Array

## Problem
> Suppose a sorted array is rotated at some pivot unknown to you beforehand.
>
> (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
>
> You are given a target value to search. If found in the array return its index, otherwise return -1.
>
> You may assume no duplicate exists in the array.

在一个偏移过的有序数组里面查找。

## Solution

- Search

  既然偏移过，如果我们可以找到数组是从哪里偏移的，我们就可以把下标映射回原来有序的数组，
  那么我们就可以直接使用二分查找了有木有。记得把结果再映射回来。
  有序的位置有一个特点，就是前一个数比后一个数大嘛，我们先找到这个地方。

  不过这么做的话，需要遍历数组，时间复杂度是 O(n)，那还二分查找个毛啊，直接搜索就得了。
  换句话说也就是说我们丧失了二分查找的优势。

- Binary Search

  不过呢，想二分也是可以的。

  二分的话关键是每次都可以扔掉一半元素，也就是每次比较都可以确定要找的数在左右哪一部分。
  平均切分这个偏移过的数组，有两种情况：
  - 左边是有序的（第一个数比中间的数小）
    - 如果 target 在左边，二分查找左边（普通的二分）
    - 否则找右边（和该问题的情况一样了）

  - 右边是有序的（同上）

## Code

### Python

```python
# wait a minute
```

### C++

```cpp
class Solution {
public:
    int search(int A[], int n, int target) {
        int low = 0, high = n;
        while (low < high) {
            int mid = (low + high) / 2;
            if (target == A[mid]) {
                return mid;
            }

            // 左边有序
            if (A[low] < A[mid]) {
                if (A[low] <= target && target < A[mid]) {
                    high = mid;
                } else {
                    low = mid + 1;
                }
            } else {
                if (A[mid] < target && target <= A[high - 1]) {
                    low = mid + 1;
                } else {
                    high = mid;
                }
            }
        }
        return -1;
    }
};
```
