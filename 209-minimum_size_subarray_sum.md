# 209-Minimum Size Subarray Sum

## Problem

> Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

> For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

## Solution

滑动窗口法。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size();
        
        int begin = 0; 
        int end = 0;
        int cur_sum = 0;
        int result = n+1;
        
        while (end < n) {
            while (end < n && cur_sum < s) {
                cur_sum += nums[end];
                end++;
            }
            if (cur_sum < s) {
                return result == n+1 ? 0 : result;
            }
            while (begin < end && cur_sum - nums[begin] >= s) {
                cur_sum -= nums[begin];
                begin++;
            }
            result = min(result, end - begin);
            cur_sum -= nums[begin];
            begin++;
        }
        return result == n+1 ? 0 : result;
    }
};
```