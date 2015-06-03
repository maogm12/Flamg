# 213-House Robber II

## Problem

> ***Note***: This is an extension of House Robber.

> After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

> Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

## Solution

由于第一间房子和最后一间房子相邻，那么可以分情况考虑。

- 不抢第一间房子，那么可以抢最后一间房子。
- 抢第一件房子，不抢最后一间房子。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0 || n == 1) {
            return n == 1 ? nums[0] : 0;
        }
        
        vector<int> dp(n, 0);
        int max_value = nums[0];
        
        for (int i = 1; i < n; i++) {
            dp[i] = max(dp[i-1], i-2 >= 0 ? dp[i-2] + nums[i]: nums[i]);
            max_value = max(max_value, dp[i]);
        }
        fill(dp.begin(), dp.end(), 0);
        
        dp[0] = nums[0];
        for (int i = 1; i < n-1; i++) {
            dp[i] = max(dp[i-1], i-2 >= 0 ? dp[i-2] + nums[i]: nums[i]);
            max_value = max(max_value, dp[i]);
        }
        return max_value;
    }
};
```