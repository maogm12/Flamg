# 022-Generate Parentheses

## Problem

> Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

> For example, given n = 3, a solution set is:

> "((()))", "(()())", "(())()", "()(())", "()()()"

## Solution

- 回溯，在形成结果字符串的过程中，需要根据已有的结果字符串中的左括号和右括号的数目来确定下一个需要添加的括号。如开始时字符串为空，只能添加左括号；又如`((`，若n=3，那么此时可能添加左括号，也可能添加右括号。因此，需要记录当前串所拥有的左括号和右括号的数目。

## Code

### Python

```python
class Solution:
    # @param n, an integer
    # @return a string[]
    def generateParenthesis(self, n):
        self.results = []
        self.parent_hesis('', 0, 0, n)
        return self.results
    
    def parent_hesis(self, result, pos, neg, n):
        if pos == n and neg == n:
            self.results.append(result)
            return
        if pos > neg:
            if pos < n:
                self.parent_hesis(result + '(', pos+1, neg, n)
            self.parent_hesis(result + ')', pos, neg+1, n)
        elif pos == neg:
            self.parent_hesis(result + '(', pos+1, neg, n)
```

### C++

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        results.clear();
        parent_hesis("", 0, 0, n);
        return results;
    }
    
    void parent_hesis(string result, int pos, int neg, int n) {
        if (pos == n && neg == n) {
            results.push_back(result);
            return;
        }
        if (pos > neg) {
            if (pos < n) {
                parent_hesis(result + "(", pos+1, neg, n);
            }
            parent_hesis(result + ")", pos, neg+1, n);
        } else if (pos == neg) {
            parent_hesis(result + "(", pos+1, neg, n);
        }
    }
private:
    vector<string> results;
};
```