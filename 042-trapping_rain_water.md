# 042-Trapping Rain Water

## Problem

> Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

> For example,

> Given `[0,1,0,2,1,0,1,3,2,1,2,1]`, return `6`.

> ![rainwatertrap](./images/rainwatertrap.png)

> The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

城墙状容器能装多少水

## Solution

- 搜索

    我们可以注意到，如果以某一个柱子开始，找到下一个比这个柱子高的柱子，这之间的水是很好计算的。我们可以先找到最高的那根柱子，然后从左边，右边同时往那个最高的柱子搜索，计算左边右边分别可以装多少水。

    上面那个图片的例子：

    最高点下标为 `7`，从下标 `0` 和 `11` 同时往 `7` 搜索。左边搜索过程如下：

    1. 发现 `1` 比 `0` 高，这之间装了 `0` 单位的水，把左边目前为止的最大值更新为 `1`
    2. 发现 `3` 比 `1` 高，这之间装了 `1` 单位的水，嗯，记录起来，把左边目前为止最大值更新为 `3`
    3. 依次类推，直到 `7` 为止

    右边也类似，时间复杂度为 O(n)

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() <= 2) {
            return 0;
        }

        int size = height.size();

        // 寻找最大值的下标
        int maxPos = 0, maxHeight = height[0];
        for (int i = 1; i < size; ++i) {
            if (height[i] > maxHeight) {
                maxHeight = height[i];
                maxPos = i;
            }
        }

        int water = 0;

        // 搜索左边
        int left = 1, leftWater = 0, leftMax = 0;
        while (left <= maxPos) {
            if (height[left] <= height[leftMax]) {
                leftWater += height[leftMax] - height[left];
            } else {
                leftMax = left;
                water += leftWater;
                leftWater = 0;
            }
            ++left;
        }
        water += leftWater;

        // 搜索右边
        int right = size - 2, rightWater = 0, rightMax = size - 1;
        while (right >= maxPos) {
            if (height[right] <= height[rightMax]) {
                rightWater += height[rightMax] - height[right];
            } else {
                rightMax = right;
                water += rightWater;
                rightWater = 0;
            }
            --right;
        }
        water += rightWater;

        return water;
    }
};
```
