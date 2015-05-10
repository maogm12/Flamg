# 059-Spiral Matrix II

## Problem

> Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

> For example,
Given n = 3,

> You should return the following matrix:
>
```
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```

## Solution

与054题类似，只不过是倒过来，由拷贝值变成了赋值。

## Code

### Python

```python

zyx太懒了，这个题不想写python版了。

```

### C++

```cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<int> rows(n, 0);
        vector<vector<int> > matrix(n, rows);
        
        int k = (n-1) / 2;
        int v = 1;
        for (int i = 0; i <= k; i++) {
            int start = i;
            int end = n - i - 1;
            
            for (int j = start; j <= end; j++) {
                matrix[start][j] = v;
                v++;
            }
            for (int j = start + 1; j <= end; j++) {
                matrix[j][end] = v;
                v++;
            }
            if (start == end) {
                break;
            }
            for (int j = end - 1; j >= start; j--) {
                matrix[end][j] = v;
                v++;
            }
            for (int j = end - 1; j > start; j--) {
                matrix[j][start] = v;
                v++;
            }
        }
        return matrix;
    }
};
```