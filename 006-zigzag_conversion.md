# 006-ZigZag Conversion

## Question
> The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

> ```
P   A   H   N
A P L S I I G
Y   I   R
> ```

> And then read line by line: `"PAHNAPLSIIGYIR"`

> Write the code that will take a string and make this conversion given a number of rows:

> ```
string convert(string text, int nRows);
> ```

> `convert("PAYPALISHIRING", 3)` should return `"PAHNAPLSIIGYIR"`.

一下一上的把字符串折起来

## Solution

这题要好好观察折起来的字符串特点

1. 原字符串可以看成每 `numRows + numRows - 2` 个字符一组，每组里面折一下
2. 不是等长折，折起来右边一般比左边一半短两个字符

我们可以一行一行处理，找好对应关系就不难

## Code

### Python
来不及了

### C++
```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1) {
            return s;
        }
        
        int segSize = numRows + numRows - 2;
        int segNum = s.size() / segSize + 1;
        string result(s.size(), ' ');
        int newIndex = 0;
        for (int row = 0; row < numRows; ++row) {
            for (int segIndex = 0; segIndex < segNum; ++segIndex) {
                int oldIndex = segIndex * segSize + row;
                if (oldIndex < s.size()) {
                    result[newIndex++] = s[oldIndex];
                }
                
                if (row > 0 && row < numRows - 1) {
                    oldIndex = segIndex * segSize + segSize - row;
                    if (oldIndex < s.size()) {
                        result[newIndex++] = s[oldIndex];
                    }
                }
            }
        }
        
        return result;
    }
};
```
