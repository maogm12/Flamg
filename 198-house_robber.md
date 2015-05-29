# 198-House Robber

## Problem

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

> Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

## Solution

- 递推，用一个数组来保存以商店i为结尾的结果，那么
	`dp[i] = max(dp[0...i-2]) + nums[i]`

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) {
            return 0;
        }
        vector<int> dp(size, 0);
        int i = 0;
        for (; i < min(size, 2); i++) {
            dp[i] = nums[i];
        }
        int max_value = 0;
        for (; i < size; i++) {
            max_value = max(dp[i-2], max_value);
            dp[i] = nums[i] + max_value;
        }
        for (; i - 2 < size; i++) {
            max_value = max(dp[i-2], max_value);
        }
        
        return max_value;
    }
};
```