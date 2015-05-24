# 085-Maximal Rectangle

## Problem

> Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

## Solution

- 暴力算法，从矩阵中随机找出两个元素，作为长方形的左上角和右下角，检测该长方形是否符合条件。时间复杂度为O(n<sup>4</sup>)，当然，如果矩阵中0的数目比较多的话，可以大量的剪枝。

- 优化一下，我们遍历每个元素，找出以该元素为右下角的所有合法矩形，为了存储起见，我们不必保存所有合法矩形，子矩形不必保存，换句话说，保存的矩形要尽可能的延展。那么在求下一个元素时，可以利用之前的计算结果。比如，`dp[i][j]`可以利用`dp[i-1][j]`和`dp[i][j-1]`的结果。

- 再优化，会发现，其实求`dp[i][j]`只需要依赖`dp[i-1][j]``或dp[i][j-1]`一个就够了，比如根据`dp[i][j-1]`来求`dp[i][j]`，那么只需要找到`matrix[0...i][j]`中以i为结尾的连续1的长度，然后将其和dp[i][j-1]一起考虑。如何考虑呢？**那就是Maximal Rectangle in Histogram题目**。
	
> BTW， 我只想到第二步，最后与Histogram题目思路的结合没想到，可能写矩阵的dp考虑`（dp[i][j-1], dp[i-1][j], dp[i-1][j-1]）`三元组考虑的多了，产生了思维盲区，从没想过只和一个前面元素相关的情况，(吐槽：只和前面一个有关就不叫dp了，TT)

## Code

### Python

```python
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        level_heights = [[0 for j in range(n+1)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    level_heights[i][j] = 1
                    if i > 0:
                        level_heights[i][j] += level_heights[i-1][j]
        max_area = 0
        for i in range(m):
            max_area = max(max_area, self.get_max_area(level_heights[i]))
        return max_area
    
    def get_max_area(self, heights):
        stack = []
        len_heights = len(heights)
        max_area = 0
        i = 0
        while i < len_heights:
            if len(stack) == 0 or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tmp_height = heights[stack.pop()]
                tmp_area = tmp_height * i if len(stack) == 0 else tmp_height * (i- stack[-1] - 1)
                max_area = max(tmp_area, max_area)
        return max_area

```

### C++

```cpp
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) {
            return 0;
        }
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> height_level(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    height_level[i][j] = 1;
                    if (i > 0) {
                        height_level[i][j] += height_level[i-1][j];
                    }
                 }
            }
        }
        int max_area = 0;
        for (int i = 0; i < m; i++) {
            max_area = max(max_area, largestRectangleArea(height_level[i]));
        }
        return max_area;
    }
    int largestRectangleArea(vector<int>& height) {
        stack<int> s;
        height.push_back(0);
        int i = 0;
        int max_area = 0;
        while (i < height.size()) {
            if (s.empty() || height[i] >= height[s.top()]) {
                s.push(i++);
            } else {
                int tmp_index = s.top();
                s.pop();
                int tmp_area = s.empty() ? height[tmp_index] * i : height[tmp_index] * (i - s.top() - 1);
                max_area = max(tmp_area, max_area);
            }
        }
        return max_area;
    }
};
```