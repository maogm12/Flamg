# 045-Jump Game II

## Problem

> Given an array of non-negative integers, you are initially positioned at the first index of the array.

> Each element in the array represents your maximum jump length at that position.

> Your goal is to reach the last index in the minimum number of jumps.

> For example:
Given array A = `[2,3,1,1,4]`

> The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

## Solution

使用一个数组steps来保存当前所达到的范围内的最短步数。

- 当走到一个索引index时，当前索引最短步数为steps[index]
- 那么更新steps的区间[index+1，index+nums[index]]中的值，如果步数小于之前的值，则更新。然后走向下一个index

> 注意到，本题有一个性质，那就是对于两个索引i和j，如果`i<j`，那么`steps[i] <= steps[j]`一定成立。且可以得到，若从i出发，到达的范围如果在j之后，比如说k，那么从i跳到k肯定比从j跳到k的步数要少或者等于。所以，当从i到下一个节点i+1时，只需要去更新新到达的区域的步数即可。具体请看代码。

## Code

### Python

```python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        len_nums = len(nums)
        steps = [-1 for i in range(len_nums)]
        steps[0] = 0
        i = 0
        max_index = 0
        while i < len_nums and i <= max_index:
            if max_index < i + nums[i]:
                v = steps[i]
                for j in range(max_index+1, min(len_nums-1, i + nums[i]) + 1):
                    steps[j] = v + 1
                max_index = i + nums[i]
            i += 1
        return steps[-1]
```

### C++

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        int len_num = nums.size();
        vector<int> steps(len_num, -1);
        int i = 0;
        int max_index = 0;
        steps[0] = 0;
        while (i < len_num && i <= max_index) {
            if (max_index < i + nums[i]) {
                int step = steps[i];
                
                for (int j = max_index+1; j <= min(i+nums[i], len_num-1); j++) {
                    steps[j] = step + 1;
                }
                max_index = i + nums[i];
            }
            i++;
        }
        return steps[len_num - 1];
    }
};
```