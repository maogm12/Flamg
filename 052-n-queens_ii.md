# 052-N-Queens II

## Problem

> Follow up for N-Queens problem.

> Now, instead outputting board configurations, return the total number of distinct solutions.
>
![8-queens](./images/8-queens.png)

## Solution

把051的回溯代码改一下，把添加结果的代码改为结果数目加1即可。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int totalNQueens(int n) {
        string s(n, '.');
        vector<string> result(n, s);
        results_num = 0;
        solve(result, 0, n);
        return results_num;
    }

    void solve(vector<string> &result, int index, int n) {
        if (index == n) {
            results_num++;
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

    /* challenge
    bool check(vector<string>& result, int i, int j, int n) {
        for (int row = 1; row <= i; ++row) {
            if (result[i - row][j] == 'Q' || (j - row >= 0 && result[i - row][j - row] == 'Q') ||
                (j + row < n && result[i - row][j + row] == 'Q')) {
                return false;
            }
        }
        return true;
    }
    */
private:
    int results_num;
};

```
