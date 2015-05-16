# 034-Search for a Range

## Problem

> Given a sorted array of integers, find the starting and ending position of a given target value.

> Your algorithm's runtime complexity must be in the order of O(log n).

> If the target is not found in the array, return [-1, -1].

> For example,
Given `[5, 7, 7, 8, 8, 10]` and target value `8`,
return `[3, 4]`.

## Solution

- 我最直观的想法是先用二分查找找到target，然后向两边遍历找到上限和下限，但是这种方法的复杂度可能到O(n)，即数组中全都是target的时候。
- 所以觉得还是使用二分查找找上限和下限比较好。

## Code

### Python

```python
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        len_nums = len(nums)
        lower = self.lower_bound(nums, 0, len_nums-1, target)
        upper = self.upper_bound(nums, 0, len_nums-1, target)
        return [lower, upper]
    
    def lower_bound(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) / 2
            if mid == start:
                if nums[mid] == target:
                    return mid
                if nums[end] == target:
                    return end
                return -1
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1
        return -1
    
    def upper_bound(self, nums, start, end, target):
        while start <= end:
            mid = (start + end) / 2
            if mid == start:
                if nums[end] == target:
                    return end
                if nums[mid] == target:
                    return mid
                return -1
            if nums[mid] <= target:
                start = mid
            else:
                end = mid - 1
        return -1
```

### C++

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int len_num = nums.size();
        int lower = lower_bound(nums, 0, len_num - 1, target);
        int upper = upper_bound(nums, 0, len_num - 1, target);
        vector<int> result;
        result.push_back(lower);
        result.push_back(upper);
        return result;
    }
    int lower_bound(vector<int> &nums, int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (mid == start) {
                if (nums[mid] == target) {
                    return mid;
                }
                if (nums[end] == target) {
                    return end;
                }
                return -1;
            }
            if (nums[mid] >= target) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return -1;
    }
    int upper_bound(vector<int> &nums, int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (mid == start) {
                if (nums[end] == target) {
                    return end;
                }
                if (nums[mid] == target) {
                    return mid;
                }
                return -1;
            }
            if (nums[mid] <= target) {
                start = mid;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }
};
```