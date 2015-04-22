# 048-Rotate Image

## Problem

> You are given an n x n 2D matrix representing an image.

> Rotate the image by 90 degrees (clockwise).

> Follow up:

> Could you do this in-place?

顺时针旋转一个方阵

## Solution

- 那就转呗

    关键是确定转动的点，对于一个 `n x n` 的方阵，有一个点 `(x, y)`，
    其逆时针对应的其他三个点为
    `(y, n - x)`,
    `(n - x, n - y)`,
    `(n - y, x)`

    看下面两个例子，分别对应奇数边和偶数边的情况：

    ```
    奇数        偶数
    11122       1122
    11122       1122
    44522       4433
    44333       4433
    44333
    ```

    我们对左上角的 1/4 区域里面的点都顺时针转动到相应的区域即可。
    即把 1 换到 2，2 换到 3，3 换到 4，4 换到 1

## Code

### Python

```python
# foo bar
```

### C++

```cpp
class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        int size = matrix.size();
        if (size <= 1) {
            return;
        }
        int width = size % 2 == 0 ? size / 2 : size / 2 + 1;
        int height = size / 2;
        for (int x = 0; x < width; ++x) {
            for (int y = 0; y < height; ++y) {
                rotate(matrix, x, y, size);
            }
        }
    }

    // 辅助函数，转动一个点
    void rotate(vector<vector<int> > &matrix, int x, int y, int size) {
        int temp = matrix[y][x];
        matrix[y][x] = matrix[size - 1 - x][y];
        matrix[size - 1 - x][y] = matrix[size - 1 - y][size - 1 - x];
        matrix[size - 1 - y][size - 1 -x] = matrix[x][size - 1 - y];
        matrix[x][size - 1 - y] = temp;
    }
};
```

## Challenge Code

> 咳咳，我是发言者zyx，解法没有任何问题，但是代码中判断width的奇偶性确实不必要的。
因而，代码如下更有简洁。

### cpp code of challege

```cpp
class Solution {
public:
    void rotate(vector<vector<int> > &matrix) {
        int n = matrix.size();
        for (int index = 0; index < n/2; index++) {
            for (int i = index; i < n - index - 1; i++) {
                int tmp = matrix[index][i];
                matrix[index][i] = matrix[n-i-1][index];
                matrix[n-i-1][index] = matrix[n-index-1][n-i-1];
                matrix[n-index-1][n-i-1] = matrix[i][n-index-1];
                matrix[i][n-index-1] = tmp;
            }
        }
    }
};
```
