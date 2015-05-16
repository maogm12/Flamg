# 118-Pascal's Triangle

## Problem

> Given numRows, generate the first numRows of Pascal's triangle.

> For example, given numRows = 5,
Return
>
```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

## Solution

不解释，看代码

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> results;
        for (int i = 0; i < numRows; i++) {
            if (i == 0) {
                results.push_back(vector<int> {1});
            } else {
                vector<int> new_row(i+1, 1);
                for (int j = 1; j < i; j++) {
                    new_row[j] = results[i-1][j] + results[i-1][j-1];
                }
                results.push_back(new_row);
            }
        }
        return results;
    }
};
```