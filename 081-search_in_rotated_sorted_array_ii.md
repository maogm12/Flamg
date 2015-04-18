# 081-Search in Rotated Sorted Array II

## Problem

> Follow up for "Search in Rotated Sorted Array":
> What if duplicates are allowed?
>
> Would this affect the run-time complexity? How and why?
>
> Write a function to determine if a given target is in the array.

偏转有序数组查找升级版！这里这个数组允许有重复元素出现。

## Solution

- Brute-Force

    还是找出偏移位置那个逗逼方法，还不如顺序查找。。。

    时间复杂度 O(n)

- Binary Search

    前面不允许重复元素的那个题目，我们说可以用二分查找，如果前半段有序，
    （即开头的小于中间的，A[low] < A[mid]），然后判断 target 是否在这一段里面，在的话，
    搜这一段，否则搜另外一段；后半段的情况类似。

    允许重复的这个我们尝试直接 A[low] <= A[mid]，因为有重复的嘛，
    但是这玩意儿不能确定前段有序！！！（比如：1,2,3,1,1,1,1）

    我们可以这么处理，先不判断 = 的情况，那么我们是可以判断这段是有序的，
    如果相等的话，把搜索范围缩小一点点。。。看代码！！



## Code

### Python

```python
# wait a minute.
```

### C++

```cpp
class Solution {
public:
    bool search(int A[], int n, int target) {
        int low = 0, high = n;
        while (low < high) {
            const int mid = (low + high) / 2;
            if (target == A[mid]) {
                return true;
            }

            if (A[low] < A[mid]) {
                // 左边有序哈！！！
                if (A[low] <= target && target < A[mid]) {
                    high = mid;
                } else {
                    low = mid + 1;
                }
            } else if (A[low] > A[mid]) {
                // 右边有序哈！！！
                if (A[mid] < target && target <= A[high - 1]) {
                    low = mid + 1;
                } else {
                    high = mid;
                }
            } else {
                // 神来之笔！！！
                low++;
            }
        }

        return false;
    }
};
```
