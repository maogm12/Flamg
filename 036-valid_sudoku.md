# 036-Valid Sudoku

## Problem

> Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules](http://sudoku.com.au/TheRules.aspx).
>
> The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
>
> ![A partially filled sudoku which is valid.](./images/250px-Sudoku-by-L2G-20050714_svg.png)
>
> A partially filled sudoku which is valid.
>
> Note:
>
> A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

判断数独是否合法，可能只填了一半。

## Solution

- 哈希表

    这个题没什么讲的，每行每列每个 cell 9 个数里面不要出现重复的数字就 OK 了。可以使用哈希表记录已经访问过的元素。

## Code

### Python

```python
# blah blah
```

### C++

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char> > &board) {
        unordered_map<char, bool> validator;

        for (int i = 0; i < 9; ++i) {
            // row
            resetValidator(validator);
            for (int j = 0; j < 9; ++j) {
                char ch = board[i][j];
                if (ch == '.') {
                    continue;
                }
                if (validator[ch]) {
                    return false;
                } else {
                    validator[ch] = true;
                }
            }

            // col
            resetValidator(validator);
            for (int j = 0; j < 9; ++j) {
                char ch = board[j][i];
                if (ch == '.') {
                    continue;
                }
                if (validator[ch]) {
                    return false;
                } else {
                    validator[ch] = true;
                }
            }

            // cell
            resetValidator(validator);
            for (int j = 0; j < 9; ++j) {
                char ch = board[i/3*3 + j/3][i%3*3 + j%3];
                if (ch == '.') {
                    continue;
                }
                if (validator[ch]) {
                    return false;
                } else {
                    validator[ch] = true;
                }
            }
        }

        return true;
    }

    void resetValidator(unordered_map<char, bool> &validator) {
        for (char c = '1'; c <= '9'; ++c) {
            validator[c] = false;
        }
    }
};
```
