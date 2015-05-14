# 075-Sort Colors

## Problem

> Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

> Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

> **Note**:

> You are not suppose to use the library's sort function for this problem.

## Solution

三指针法，由于只有三个值，可以保存0的索引a和2的索引c，在a位置之前都是0，在c位置之后都是2。

初始化时，`a=0,c=len-1`，那么从a开始，遍历到c。分为三种情况：
- 当前数字等于1，继续遍历
- 当前数字等于2，将当前数字与c位置数字交换，c左移一个位置
- 当前数字等于0，将当前数字与a位置数字交换，（注意，此时a位置数字只可能是1，具体原因找个例子一推便知），a右移一个位置。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int len_nums = nums.size();
        int zero_index = 0;
        int two_index = len_nums - 1;
        int i = 0;
        while (i <= two_index) {
            if (nums[i] == 0) {
                nums[i++] = nums[zero_index];
                nums[zero_index++] = 0;
            } else if (nums[i] == 2) {
                nums[i] = nums[two_index];
                nums[two_index--] = 2;
            } else {
                i++;
            }
        }
    }
};
```