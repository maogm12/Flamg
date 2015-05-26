# 037-Sudoku Solver

## Problem

> Write a program to solve a Sudoku puzzle by filling the empty cells.

> Empty cells are indicated by the character '.'.

> You may assume that there will be only one unique solution.
> 
> A sudoku puzzle...
>
![](./images/250px-Sudoku-by-L2G-20050714.svg.png)
>
> ...and its solution numbers marked in red.
> 
![](./images/250px-Sudoku-by-L2G-20050714_solution.svg.png)

## Solution

- 回溯
	- 找到一个空格
	- 找出这个空格所有合法的数，
		- 从合法的数中选一个
		- 递归处理，如果成功则记录，如果不成功，则返回上一步

## Code

### Python

```python
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
	def solveSudoku(self, board):
		num_board = [[ 0  for j in range(9)] for i in range(9)]
		for i in range(9):
			for j in range(9):
				if board[i][j] != '.':
					num_board[i][j] = ord(board[i][j]) - ord('0')
		self.solve(num_board)
		for i in range(9):
			str_row = [str(v) for v in num_board[i]]
			str_row = ''.join(str_row)
			board[i] = str_row
		# print_matrix(board)
		
	def find_one(self, num_board):
		for i in range(9):
			for j in range(9):
				if num_board[i][j] == 0:
					return i,j
		return -1, -1

	def solve(self, num_board):
		i,j = self.find_one(num_board)
		if i == -1 and j == -1:
			return True
		for v in range(1,10):
			if self.check(num_board, v, i, j):
				num_board[i][j] = v
				if self.solve(num_board):
					return True
				num_board[i][j] = 0
		

	def check(self, num_board, v, i, j):
		for k in range(9):
			if num_board[i][k] == v:
				return False
		for k in range(9):
			if num_board[k][j] == v:
				return False
		part_i = i / 3
		part_j = j / 3
		for x in range(3):
			for y in range(3):
				if num_board[ part_i*3+x ][ part_j*3+y ] == v:
					return False
		return True
```

### C++

```cpp
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
    void find_blank(vector<vector<char>> &board, int &x, int &y) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    x = i;
                    y = j;
                    return;
                }
            }
        }
    }
    bool solve(vector<vector<char>> &board) {
        int x = -1;
        int y = -1;
        find_blank(board, x, y);
        if (x == -1 && y == -1) {
            return true;
        }
        for (int k = 1; k <= 9; k++) {
            board[x][y] = '0' + k;
            if (check_board(board, x, y) && solve(board)) {
                return true;
            }
            board[x][y] = '.';
        }
        return false;
    }
    bool check_board(vector<vector<char>> &board, int x, int y) {
        for (int i = 0; i < 9; i++) {
            if (i != x && board[i][y] == board[x][y]) {
                return false;
            }
        }
        for (int j = 0; j < 9; j++) {
            if (j != y && board[x][j] == board[x][y]) {
                return false;
            }
        }
        for (int i = x/3 * 3; i < (x/3+1) * 3; i++) {
            for (int j = y/3 * 3; j < (y/3+1) * 3; j++) {
                if (i == x && j == y) {
                    continue;
                }
                if (board[i][j] == board[x][y]) {
                    return false;
                }
            }
        }
        return true;
    }
    
};
```