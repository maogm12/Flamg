# 120-Triangle

## Problem

> Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

> For example, given the following triangle
>
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
>
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

> **Note**:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

## Solution

典型的动规题目，三角形的每一层都可以根据上一层的路径最小值求出，递推公式为:
`dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]`

从上往下推，有两个缺点：

- 需要解决当前层的最后一个元素的边界判断问题
- 在最后一层判断结束后，需要再遍历最后一层求出最小值。

而从下往上的求解，则没有此问题。而递推式相应的变化为：
`dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]`

将动规所需的空间合并到三角形数据本身里，则可以减少内存至O(1)。

## Code

### Python 自底向上

```python
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        i = n-2
        while i >= 0:
            for j in range(0, i+1):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
            i -= 1
        return triangle[0][0]
```

### python 自顶向下

```python
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
		if len(triangle) == 1:
			return triangle[0][0]
		for i in range(1, len(triangle)):
			for j in range(i+1):
				if j == 0:
					triangle[i][j] += triangle[i-1][j]
				elif j == i:
					triangle[i][j] += triangle[i-1][j-1]
				else:
					triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
		return min(triangle[-1])

```

### C++

```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int> > &triangle) {
        int n = triangle.size();
        for (int i = n-2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j];
            }
        }
        return triangle[0][0];
    }
};
```