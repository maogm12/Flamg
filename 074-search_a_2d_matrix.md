# 074-Search a 2D Matrix

## Problem

> Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

> Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

> Consider the following matrix:
> 
```
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
```
Given target = 3, return true.

## Solution

- 最直观的，可能会想到先搜索行，找到一行，使得该行的第一个元素小于等于target且下一行的第一个元素大于等于target。然后再寻找改行中是否有这个值。当然，两个搜索都用二分查找。

- 因为下一行的第一个元素大于当前航的最后一个元素，所以可以把整个矩阵当做一个大的排序数组，在此基础上做查找，比上一种方法简便很多。

> 注意，二分查找也分递归版和迭代版，本文也全部给出。


## Code

### Python

```python

```

### C++ for row-colunmu binary search

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int row = binary_search_row(matrix, target, 0, m-1);
        return binary_search_ele(matrix[row], target, 0, n-1);
    }
    bool binary_search_ele(vector<int> &row, int target, int start, int end) {
        if (start > end) {
            return false;
        }
        if (end - start <= 1) {
            if (row[start] == target) {
                return true;
            }
            return row[end] == target;
        }
        int mid = (start + end) / 2;
        if (row[mid] == target) {
            return mid;
        } else if (row[mid] < target) {
            return binary_search_ele(row, target, mid+1, end);
        } else if (row[mid] > target) {
            return binary_search_ele(row, target, start, mid-1);
        }
    }
    int binary_search_row(vector<vector<int>>& matrix, int target, int start_row, int end_row) {
        if (start_row == end_row) {
            return start_row;
        } else if (end_row - start_row == 1) {
            if (matrix[end_row][0] <= target) {
                return end_row;
            }
            return start_row;
        }
        int mid = (start_row + end_row) / 2;
        if (matrix[mid][0] > target) {
            return binary_search_row(matrix, target, start_row, mid - 1);
        } else {
            return binary_search_row(matrix, target, mid, end_row);
        }
    }
};
```

### C++ for directly binary search（Recursive）

```
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        return binary_search_directly(matrix, target, 0, m*n-1, n);
    }
    
    bool binary_search_directly(vector<vector<int>> &matrix, int target, int start, int end, int n) {
        int mid = (start + end) / 2;
        int value = matrix[mid / n][mid % n];
        if (mid == start) {
            if (value == target) {
                return true;
            }
            return matrix[end / n][end % n] == target;
        }
        if (value < target) {
            return binary_search_directly(matrix, target, mid + 1, end, n);
        } else if (value > target) {
            return binary_search_directly(matrix, target, start, mid - 1, n);
        } else if (value == target) {
            return true;
        }
        
    }
    
};
```

### C++ for directly binary search (iter)

```
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int start = 0;
        int end = m * n - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            int value = matrix[mid / n][mid % n];
            if (mid == start) {
                if (value == target) {
                    return true;
                }
                return matrix[end / n][end % n] == target;
            }
            if (value == target) {
                return true;
            } else if (value > target) {
                end = mid - 1;
            } else if (value < target) {
                start = mid + 1;
            }
        }
        return false;
    }
};
```