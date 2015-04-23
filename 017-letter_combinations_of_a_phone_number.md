# 017-Letter Combinations of a Phone Number

## Problem

> Given a digit string, return all possible letter combinations that the number could represent.

> A mapping of digit to letters (just like on the telephone buttons) is given below.

> ![A partially filled sudoku which is valid.](./images/200px-Telephone-keypad2.svg.png)

>
```
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
**Note**:
Although the above answer is in lexicographical order, your answer could be in any order you want.

## Solution

- 递归
	- 首先，定义好数字和字母的对应。
	- 找到第一个数字所对应的字母们，遍历每个字母，将其添加到结果串中，然后找第二个数字。以此类推。

## Code

### Python

```python
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        letters_map = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.results = []
        if len(digits) == 0:
            return self.results
        self.combine(digits, 0, '', letters_map)
        return self.results
    
    def combine(self, digits, index, result, letters_map):
        if index == len(digits):
            self.results.append(result)
            return
        ch = digits[index]
        ch_index = ord(ch) - ord('0') - 2
        for letter in letters_map[ch_index]:
            self.combine(digits, index+1, result+letter, letters_map)
```

### C++

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        string letters_map[] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        string result = "";
        results.clear();
        if (digits.length() == 0) {
            return results;
        }
        letter_combine(digits, 0, result, letters_map);
        return results;
    }
    void letter_combine(const string &digits, const int index, string &result, string letters_map[]) {
        if (index == digits.length()) {
            results.push_back(result);
            return;
        }
        char ch = digits[index];
        int ch_index = ch - '0' - 2;
        string letters = letters_map[ch_index];
        for (int i = 0; i < letters.length(); i++) {
            ch = letters[i];
            result.push_back(ch);
            letter_combine(digits, index+1, result, letters_map);
            result.pop_back();
        }
    }
private:
    vector<string> results;
};
```