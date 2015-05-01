# 006ZigZag Conversion

## Question
> The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

> ```
P   A   H   N
A P L S I I G
Y   I   R
> ```

> And then read line by line: "PAHNAPLSIIGYIR"   
> Write the code that will take a string and make this conversion given a number of rows:

> string convert(string text, int nRows);   
> convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

## Solution

一下一上的把字符串折起来

## Code

### Python

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
