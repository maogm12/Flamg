# 079-Word Search

## Problem

> Given a 2D board and a word, find if the word exists in the grid.

> The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

> For example,
Given board =
>
```
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
```

> word = `"ABCCED"`, -> returns true,
> 
> word = `"SEE"`, -> returns true,
> 
> word = `"ABCB"`, -> returns false.

## Solution

回溯法，判断一个情况是否通过，比如如上图中，寻找`ABCCED`，当找到`ABCE`时，与`ABCCED`的前四个并不匹配，于是字符串返回到`ABC`的状态，继续寻找，发现矩阵的`C`下面有一个`C`正好匹配，于是`ABCC`匹配好了，再继续向后匹配。

具体，看代码！

## Code

### Python

```python
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.is_exist(board, i, j, word, 0, visited):
                        return True
        return False
    
    def is_exist(self, board, i, j, word, index, visited):
        if index == len(word):
            return True
        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
            
        if visited[i][j] == 0 and board[i][j] == word[index]:
            visited[i][j] = 1
            if self.is_exist(board, i-1, j, word, index+1, visited):
                return True
            if self.is_exist(board, i+1, j, word, index+1, visited):
                return True
            if self.is_exist(board, i, j-1, word, index+1, visited):
                return True
            if self.is_exist(board, i, j+1, word, index+1, visited):
                return True
            visited[i][j] = 0
        return False
```

### C++

```cpp

```