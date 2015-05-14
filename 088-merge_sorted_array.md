# 088-Merge Sorted Array

## Problem

> Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

> *Note:*

> You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

## Solution

因为 `nums1` 有足够空间，所以我们从后往前填数即可，注意边界哦！比如某个数组已经空了怎么处理 

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int i = m + n - 1; i >= 0; --i) {
            if (n == 0) {
                break;
            }

            if (m > 0 && nums1[m - 1] > nums2[n - 1]) {
                nums1[i] = nums1[m - 1];
                --m;
            } else {
                nums1[i] = nums2[n - 1];
                --n;
            }
        }
    }
};
```
