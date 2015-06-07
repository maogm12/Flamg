# 215-Kth Largest Element in an Array

## Problem

> Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

> For example,
Given `[3,2,1,5,6,4]` and k = 2, return 5.

> Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

## Solution

使用快排的思想，根据一个数，将数组根据该数划分为两部分，并得到该数所在的位置，
- 如果位置等于k，就找到了第k大，
- 如果位置大于k，那么就在前半部分数组中继续找第k大。
- 如果位置小于k，加入说是i，那么就在后半部分数组中找第k-i大的数。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return find_kth(nums, k, 0, nums.size()-1);
    }
    int find_kth(vector<int> &A, int k, int begin, int end) {
        int b = begin, e = end;
        int tmp = A[b];
        while (b < e) {
            while (e > b && A[e] <= tmp) {
                e--;
            }
            if (b != e) {
                A[b] = A[e];
            }
            while (e > b && A[b] > tmp) {
                b++;
            }
            if (b != e) {
                A[e] = A[b];
            }
        }
        A[b] = tmp;
        if (b - begin + 1 == k) {
            return A[b];
        } else if (b-begin+1 > k) {
            return find_kth(A, k, begin, b-1);
        } else if (b-begin+1 < k) {
            return find_kth(A, k - (b-begin+1), b+1, end);
        }
    }
};
```