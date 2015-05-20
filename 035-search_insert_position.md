# 035-Search Insert Position

## Problem

> Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

> You may assume no duplicates in the array.

> Here are few examples.

> `[1,3,5,6]`, 5 → 2

> `[1,3,5,6]`, 2 → 1

> `[1,3,5,6]`, 7 → 4

> `[1,3,5,6]`, 0 → 0

## Solution

题意是如果存在返回位置，如果不存在返回插入位置。
解法则是二分查找，但关键点在于不要漏掉比target恰好大的值。

其实就是 lower_bound

## Code

### Python

```python
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        return self.binary_search(nums, 0, len(nums), target)
    def binary_search(self, nums, start, end, target):
        while start != end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start
```

### C++

```cpp
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return binary_search(nums, 0, nums.size(), target);
    }

    int binary_search(vector<int>& nums, int start, int end, int target) {
        while (start != end) {
            int mid = (start + end) / 2;
            if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return start;
    }
};
```

stl 法

```cpp
int searchInsert(vector<int>& nums, int target) {
    auto pos = lower_bound(nums.begin(), nums.end(), target);
    return distance(nums.begin(), pos);
}
```
