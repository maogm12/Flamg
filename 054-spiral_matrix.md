# 054-Spiral Matrix

## Problem

> Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

> For example,
Given the following matrix:
>
```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
>You should return `[1,2,3,6,9,8,7,4,5]`.

## Solution

本题需要先访问外圈，再访问里圈。关键点在于把索引找对。

每次访问一圈时，可将要访问的那一圈（矩形）的左上角和右下角的坐标找出来，然后按照顺序遍历一圈即可。需要注意的是，当只剩下一行或一列元素时（即左上角坐标和右下角坐标至少有一个坐标值相同）的处理。

## Code

### Python

```python
class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        result = []
        m = len(matrix) - 1
        if m == -1:
            return result
        n = len(matrix[0]) - 1
        k = min(m,n) / 2
        for i in range(k+1):
            start_x = i
            start_y = i
            end_x = n - i
            end_y = m - i
            for j in range(start_x, end_x+1):
                result.append(matrix[start_y][j])
            for j in range(start_y+1, end_y+1):
                result.append(matrix[j][end_x])
            if start_x == end_x or start_y == end_y:
                break
            for j in range(start_x, end_x)[::-1]:
                result.append(matrix[end_y][j])
            for j in range(start_y + 1, end_y)[::-1]:
                result.append(matrix[j][start_x])
        return result
```

### C++

```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int m = matrix.size() - 1;
        if (m == -1) {
            return result;
        }
        int n = matrix[0].size() - 1;
        int k = min(m,n) / 2;
        for (int i = 0; i <= k; i++) {
            int start_x = i;
            int start_y = i;
            int end_x = n-i;
            int end_y = m-i;
            
            for (int j = start_x; j <= end_x; j++) {
                result.push_back(matrix[start_y][j]);
            }
            for (int j = start_y + 1; j <= end_y; j++) {
                result.push_back(matrix[j][end_x]);
            }
            if (end_y == start_y || end_x == start_x) {
                break;
            }
            for (int j = end_x - 1; j >= start_x; j--) {
                result.push_back(matrix[end_y][j]);
            }
            for (int j = end_y - 1; j > start_y; j--) {
                result.push_back(matrix[j][start_x]);
            }
        }
        return result;
    }
};
```