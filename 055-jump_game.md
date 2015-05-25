# 055-Jump Game

## Problem

> Given an array of non-negative integers, you are initially positioned at the first index of the array.

> Each element in the array represents your maximum jump length at that position.

> Determine if you are able to reach the last index.

> For example:
>
A = `[2,3,1,1,4]`, return true.

> A = `[3,2,1,0,4]`, return false.

## Solution

一步一个脚印的向前走，看看能不能到达最后一个台阶。

## Code

### Python

```python
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        len_num = len(nums)
        if len_num == 0:
            return True
        max_index = 0
        i = 0
        while i <= max_index:
            max_index = max(i + nums[i], max_index)
            if max_index >= len_num - 1:
                return True
            i += 1
        return False

```

### C++

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len_num = nums.size();
        if (len_num == 0) {
            return true;
        }
        int max_index = 0;
        int i = 0;
        for (int i = 0; i <= max_index; i++) {
            max_index = max(i + nums[i], max_index);
            if (max_index >= len_num - 1) {
                return true;
            }
        }
        return false;
    }
};
```

Actually, when we find the current is bigger than `max_index`, we can return false

```cpp
bool canJump(vector<int>& nums) {
    int rightMost = 0;
    int size = nums.size();
    for (int i = 0; i < size; ++i) {
        if (i > rightMost ||          // i is not reachable
            rightMost >= size - 1) {  // already cover the end
            break;
        }
        rightMost = max(rightMost, i + nums[i]);
    }

    return rightMost >= size - 1;
}
```
