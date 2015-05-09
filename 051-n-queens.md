# 051-N-Queens

## Problem

> The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
>
![8-queens](./images/8-queens.png)

> Given an integer n, return all distinct solutions to the n-queens puzzle.

> Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

> For example,
There exist two distinct solutions to the 4-queens puzzle:


```
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```

## Solution

毫无疑问，回溯法解决。每一步放置一层的皇后，然后放置下一层的皇后，没有位置可以放时返回。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    vector<vector<string> > solveNQueens(int n) {
        string s(n, '.');
        vector<string> result(n, s);
        solve(result, 0, n);
        return results;
    }
    void solve(vector<string> &result, int index, int n) {
        if (index == n) {
            results.push_back(result);
        }
        for (int j = 0; j < n; j++) {
            if (check(result, index, j, n)) {
                result[index][j] = 'Q';
                solve(result, index+1, n);
                result[index][j] = '.';
            }
        }
    }
    
    bool check(vector<string> &result, int i, int j, int n) {
        int x = i-1;
        int y = j;
        int y1 = j-1;
        int y2 = j+1;
        while (x >= 0) {
            if (result[x][y] == 'Q') {
                return false;
            }
            if (y1 >= 0 && result[x][y1] == 'Q') {
                return false;
            }
            if (y2 < n && result[x][y2] == 'Q') {
                return false;
            }
            x--;
            y1--;
            y2++;
        }
        return true;
    }
    
private:
    vector<vector<string> > results;
};
```