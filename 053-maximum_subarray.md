# 053-Maximum Subarray

## Problem

> Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

> For example, given the array `[−2,1,−3,4,−1,2,1,−5,4]`,
the contiguous subarray `[4,−1,2,1]` has the largest sum = 6.

## Solution

- 暴力算法：枚举所有可能情况，复杂度O(n<sup>2</sup>).
- 动态规划：在暴力算法的基础上，考虑最大和子串的性质. 下面是分析过程：
	
	zyx君：把最大和子串从任意位置切分开，假设为a,b（a左b右），也即将整个数组也切成了两份，设为A,B。
	> 旁白君：那么，a在A中（b在B中）并不见得是最大子串。嗯，这样好像不太符合DP最优子问题的性质啊，我读书少，你不要骗我。
	
	zyx君：慌毛啊慌，我还没说完哩，a在A的最右端，b在B的最左端。那么a一定是以A的最右一个数字结尾的最大和子串，b也一定是以B的最左端数字结尾的最大和子串。否则，最大和子串必然还能变大。
	> 旁白君：听起来似乎很有道理，那么接下来是不是可以这样做：对于一个数组，将其在所有位置上都切分，然后各自找左边那个子串以最右数字为结尾的最大和数组，找右边那个子串以最左数字为结尾的最大和数组，然后两边加起来就形成一个结果，再从不同位置的不同结果中找最大值。
	
	zyx君：孺子可教也，那接下来如何优化哩？
	> 旁白君：让我想想，aha，想到了，以找左边子串以最右数字为结尾的最大和数组为例，在i位置上求值时可以利用i-1位置上得结果，递推公式是：`dp_left[i] = max(dp_left[i-1]+nums[i], nums[i])` ，右边子串上也差不多，哈哈，哥果然是智商天下无敌人见人爱花见花开的浪里小白龙，这样就齐活了。
	
	zyx君（一脸不屑）：你长得又黑又瘦，像个小黑猴一般。难道你没想到如果把所有的位置的左子串的以最右数字为结尾的最大和数组求出后，就不必要求右子串了么？因为以某个位置的数字为结尾的最大和数组的结果集合中一定已经包含了最大和数组。
	> 旁白君：嗯，你说的对，代码见真章吧，ps：不许人身攻击。



## Code

### Python

python代码直接上最终版，其他版本代码看cpp版。

```python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        pre_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            pre_sum = max(pre_sum + nums[i], nums[i])
            max_sum = max(max_sum, pre_sum)
        return max_sum
```

### C++

按照Solution中的讨论，代码应该是这样：
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len = nums.size();
        if (len == 0) {
            return 0;
        }
        vector<int> dp(len, nums[0]);
        int max_sum = dp[0];
        for (int i = 1; i < len; i++) {
            dp[i] = max(dp[i-1] + nums[i], nums[i]);
            max_sum = max(max_sum, dp[i]);
        }
        return max_sum;
    }
};
```

但其实dp数组是不需要的。只需要保存上一个值就可以了。
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int len = nums.size();
        if (len == 0) {
            return 0;
        }
        int pre_sum = nums[0];
        int max_sum = nums[0];
        for (int i = 1; i < len; i++) {
            pre_sum = max(pre_sum + nums[i], nums[i]);
            max_sum = max(max_sum, pre_sum);
        }
        return max_sum;
    }
};
```