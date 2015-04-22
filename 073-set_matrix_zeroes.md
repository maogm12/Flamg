# 073-Set Matrix Zeroes

## Problem

> Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

> Follow up:
> - Did you use extra space?
> - A straight forward solution using O(mn) space is probably a bad idea.
> - A simple improvement uses O(m + n) space, but still not the best solution.
> - Could you devise a constant space solution?

## Solution

- 哈希

    遍历所有的点，找所有的 0，记录下这些点的横竖坐标值，然后一锅端了

    空间复杂度最坏为 O(m + n)

- 复用第一排，第一列

    TT 空间复杂度 O(1) 的 NB 方法，使用第一排，第一列记录是否当前排/列是否该设置成0


## Code

### Python

```python
# blah blah
```

### C++

哈希法

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int> > &matrix) {
        int height = matrix.size();
        if (height == 0) {
            return;
        }
        int width = matrix[0].size();
        unordered_set<int> xs, ys;
        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                if (matrix[i][j] == 0) {
                    xs.insert(j);
                    ys.insert(i);
                }
            }
        }

        for (auto xit = xs.begin(); xit != xs.end(); ++xit) {
            for (int y = 0; y < height; ++y) {
                matrix[y][*xit] = 0;
            }
        }

        for (auto yit = ys.begin(); yit != ys.end(); ++yit) {
            for (int x = 0; x < width; ++x) {
                matrix[*yit][x] = 0;
            }
        }
    }
};
```

重用第一排，第一列，空间复杂度为 O(1) 法

```cpp
class Solution {
public:
    void setZeroes(vector<vector<int> > &matrix) {
        int height = matrix.size();
        if (height == 0) {
            return;
        }
        int width = matrix[0].size();

        // 关键是记录第一排，第一列是否需要置为 0
        bool resetLeft = false;
        bool resetTop = false;
        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                    if (i == 0) {
                        resetTop = true;
                    }
                    if (j == 0) {
                        resetLeft = true;
                    }
                }
            }
        }

        // 先不管第一排，第一列
        for (int x = 1; x < width; ++x) {
            for (int y = 1; y < height; ++y) {
                if (matrix[y][0] == 0 || matrix[0][x] == 0) {
                    matrix[y][x] = 0;
                }
            }
        }

        if (resetTop) {
            for (int x = 0; x < width; ++x) {
                matrix[0][x] = 0;
            }
        }
        if (resetLeft) {
            for (int y = 0; y < height; ++y) {
                matrix[y][0] = 0;
            }
        }
    }
};
```
