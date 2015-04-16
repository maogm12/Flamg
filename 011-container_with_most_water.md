#011-Container With Most Water

## Question
> Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water. 

> Note: You may not slant the container. 

这个类似于在一个柱状图里面找最大矩形的问题。比如下面这个：

```
  #
  # #
 ######
 #################
```

这个最大面积应该是最下面那排，看来找两个极大值是不靠谱的，动规也是不靠谱的。

## Solution

- Brute-Force

	暴力算法永远是存在的！！！这个嘛，我们遍历所有的情况，算出最大值。时间复杂度只有 O(n^2) 而已

- Search

	没有什么明显算法特征的题，就可以用搜索来做了。我们从两头往中间搜索，有没有发现最大的面积计算的时候是用选定的两个 `height` 中较小的算的，对于某种情况，选定 `height[i]` 和 `height[j]`，其中 `i < j, height[i] < height[j]`，那么如果我们将 `j` 继续变小，我们不可能得到更大的面积，因为矩形的宽度 `j - i` 变小了，高度最大只能是 `height[i]`，所以这个时候我们应该增大 `i`。
	
	时间复杂度是 O(n)

## Code

### Python

```python
class Solution:
    # @param height, an integer[]
    # @return an integer
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxValue = 0
        while left < right:
            if height[left] < height[right]:
                maxValue = max(maxValue, (right - left) * height[left])
                left += 1
            else:
                maxValue = max(maxValue, (right - left) * height[right])
                right -= 1
        return maxValue
```

### C++

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxValue = 0;
        while (left < right) {
            while (left < right && height[left] >= height[right]) {
                maxValue = max(maxValue, height[right] * (right - left));
                right--;
            }

			// 因为到现在右边的比左边的高，如果右边继续减小，不可能再找出更大的矩形了，所以换左边来搜索

            while (left < right && height[left] <= height[right]) {
                maxValue = max(maxValue, height[left] * (right - left));
                left++;
            }
        }
        return maxValue;
    }
};

// 代码可以进一步精简
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxValue = 0;
        while (left < right) {
			if (height[left] >= height[right]) {
				maxValue = max(maxValue, height[right] * (right - left));
				right--;
			} else {
				maxValue = max(maxValue, height[left] * (right - left));
				left++;
			}
        }
        return maxValue;
    }
};
```