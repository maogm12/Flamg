# 130-Surrounded Regions

## Problem

> Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

> A region is captured by flipping all 'O's into 'X's in that surrounded region.

> For example,
>
```
X X X X
X O O X
X X O X
X O X X
```

> After running your function, the board should be:
>
```
X X X X
X X X X
X X X X
X O X X
```

## Solution

首先，使用BFS判断是否被包围了，如果是，则将BFS队列中得所有点都改动。

## Code

### Python

```python
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == 'O':
                    is_fit, deque = self.bfs_check(board, visited, i, j)
                    if is_fit:
                        for x, y in deque:
                            board[x][y] = 'X'
        
    def bfs_check(self, board, visited, i, j):
        m = len(board)
        n = len(board[0])
        deque = [(i,j)]
        begin = 0
        is_fit = True
        while begin < len(deque):
            i, j = deque[begin]
            visited[i][j] = True
            cords = [(i+1,j), (i-1,j), (i,j+1), (i, j-1)]
            for i, j in cords:
                if 0 <= i < m and 0 <= j < n:
                    if not visited[i][j] and board[i][j] == 'O':
                        deque.append((i,j))
                        visited[i][j] = True
                else:
                    is_fit = False
            begin += 1
        return is_fit, deque
```

### C++

```cpp
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        if (m == 0) {
            return;
        }
        int n = board[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false) );
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && board[i][j] == 'O') {
                    bool is_fit = true;
                    vector<pair<int, int>> deque = bfs_check(board, visited, i, j, is_fit);
                    if (is_fit) {
                        for (auto it : deque) {
                            board[it.first][it.second] = 'X';
                        }
                    }
                }
            }
        }
    }
    
    vector<std::pair<int, int> > bfs_check(vector<vector<char>> &board, vector<vector<bool>> &visited, int i, int j, bool &is_fit) {
        int m = board.size();
        int n = board[0].size();
        vector<std::pair<int, int>> deque;
        deque.push_back(make_pair(i,j));
        int begin = 0;
        while (begin < deque.size()) {
            auto item = deque[begin];
            int x = item.first;
            int y = item.second;
            vector<int> xs {x, x, x+1, x-1};
            vector<int> ys {y+1, y-1, y, y};
            for (int k = 0; k < 4; k++) {
                x = xs[k];
                y = ys[k];
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    if (!visited[x][y] && board[x][y] == 'O') {
                        deque.push_back(make_pair(x, y));
                        visited[x][y] = true;
                    }
                } else {
                    is_fit = false;
                }
            }
            begin++;
        }
        return deque;
    }
};
```